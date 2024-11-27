#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <chrono>
#include <ctime>

// 全局变量
std::vector<int> buffer;
std::mutex mtx;
std::condition_variable cv;

// 辅助函数：获取当前时间的字符串格式
std::string getCurrentTime() {
    auto now = std::chrono::system_clock::now();
    std::time_t currentTime = std::chrono::system_clock::to_time_t(now);
    char buffer[100];
    strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", localtime(&currentTime));
    return std::string(buffer);
}

// 生产者函数
void producer(int id, int sleepTime) {
    std::this_thread::sleep_for(std::chrono::seconds(sleepTime));
    std::unique_lock<std::mutex> lock(mtx);
    int product = id;  // 生成产品，用线程号标识

    // 尝试生产
    std::cout << "[" << getCurrentTime() << "] 生产者 " << id << " 尝试生产产品 " << product << "\n";
    buffer.push_back(product);
    std::cout << "[" << getCurrentTime() << "] 生产者 " << id << " 生产了产品 " << product << "\n";

    // 显示当前缓冲区状态
    std::cout << "缓冲区: ";
    if (buffer.empty()) {
        std::cout << "空\n";
    } else {
        for (int item : buffer) std::cout << item << " ";
        std::cout << "\n";
    }

    cv.notify_all();
}

// 消费者函数
void consumer(int id, int sleepTime, std::vector<int> requiredProducers) {
    std::this_thread::sleep_for(std::chrono::seconds(sleepTime));
    std::unique_lock<std::mutex> lock(mtx);

    // 尝试消费
    std::cout << "[" << getCurrentTime() << "] 消费者 " << id << " 尝试消费产品\n";

    for (int prodId : requiredProducers) {
        cv.wait(lock, [&] { return !buffer.empty(); });

        // 找到并消费所需的产品
        auto it = std::find(buffer.begin(), buffer.end(), prodId);
        if (it != buffer.end()) {
            buffer.erase(it);
            std::cout << "[" << getCurrentTime() << "] 消费者 " << id << " 消费了生产者 " << prodId << " 的产品\n";
        } else {
            std::cout << "[" << getCurrentTime() << "] 消费者 " << id << " 未找到生产者 " << prodId << " 的产品\n";
        }

        // 显示当前缓冲区状态
        std::cout << "缓冲区: ";
        if (buffer.empty()) {
            std::cout << "空\n";
        } else {
            for (int item : buffer) std::cout << item << " ";
            std::cout << "\n";
        }
    }
}

// 主函数
int main() {
    std::ifstream file("test.txt");
    int criticalSectionCount;
    file >> criticalSectionCount;

    std::vector<std::thread> threads;
    std::string line;
    std::getline(file, line); // 跳过第一行

    while (std::getline(file, line)) {
        std::istringstream ss(line);
        int thread_id, sleep_time;
        char role;
        ss >> thread_id >> role >> sleep_time;

        if (role == 'P') {
            threads.push_back(std::thread(producer, thread_id, sleep_time));
        } else if (role == 'C') {
            std::vector<int> producer_ids;
            int producer_id;
            while (ss >> producer_id) {
                producer_ids.push_back(producer_id);
            }
            threads.push_back(std::thread(consumer, thread_id, sleep_time, producer_ids));
        }
    }

    // 等待所有线程执行完毕
    for (auto &t : threads) {
        t.join();
    }

    return 0;
}
