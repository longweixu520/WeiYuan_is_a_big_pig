#include <stdio.h>
#include <stdbool.h>

#define MAX_PROCESSES 10  // 最大进程数
#define MAX_RESOURCES 5   // 最大资源类型数

int Max[MAX_PROCESSES][MAX_RESOURCES];        // 最大需求矩阵
int Allocation[MAX_PROCESSES][MAX_RESOURCES]; // 已分配矩阵
int Need[MAX_PROCESSES][MAX_RESOURCES];       // 需求矩阵
int Available[MAX_RESOURCES];                 // 可用资源

int N, M;  // N为进程数，M为资源种类数

// 计算需求矩阵 Need
void calculate_need() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            Need[i][j] = Max[i][j] - Allocation[i][j];
        }
    }
}

// 安全性算法，检查是否存在安全序列
bool is_safe(int safe_sequence[]) {
    int Work[M];  // 临时工作资源
    bool Finish[N];  // 记录进程是否完成
    int count = 0;

    // 初始化工作资源 = 可用资源
    for (int i = 0; i < M; i++) {
        Work[i] = Available[i];
    }

    // 初始化Finish为false
    for (int i = 0; i < N; i++) {
        Finish[i] = false;
    }

    while (count < N) {
        bool found = false;
        for (int i = 0; i < N; i++) {
            // 如果进程i没有完成且其需求能被当前工作资源满足
            if (!Finish[i]) {
                bool can_allocate = true;
                for (int j = 0; j < M; j++) {
                    if (Need[i][j] > Work[j]) {
                        can_allocate = false;
                        break;
                    }
                }

                // 如果能分配
                if (can_allocate) {
                    // 假设分配资源
                    for (int j = 0; j < M; j++) {
                        Work[j] += Allocation[i][j];
                    }
                    Finish[i] = true;  // 进程i完成
                    safe_sequence[count++] = i;  // 记录安全序列
                    found = true;
                    break;
                }
            }
        }

        if (!found) {
            // 如果没有进程能够满足，则系统不安全
            return false;
        }
    }

    // 如果所有进程的 Finish 都为 true，则系统安全
    return true;
}

// 打印当前系统状态
void print_system_state() {
    printf("\n当前系统状态：\n");

    printf("Available: ");
    for (int i = 0; i < M; i++) {
        printf("%d ", Available[i]);
    }
    printf("\n");

    printf("Max矩阵:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            printf("%d ", Max[i][j]);
        }
        printf("\n");
    }

    printf("Allocation矩阵:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            printf("%d ", Allocation[i][j]);
        }
        printf("\n");
    }

    printf("Need矩阵:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            printf("%d ", Need[i][j]);
        }
        printf("\n");
    }
}

// 申请资源
bool request_resources(int process_id, int request[MAX_RESOURCES]) {
    // 检查请求是否小于等于需求
    for (int i = 0; i < M; i++) {
        if (request[i] > Need[process_id][i]) {
            printf("错误：进程 %d 请求的资源超过了最大需求！\n", process_id);
            return false;
        }
    }

    // 检查请求是否小于等于可用资源
    for (int i = 0; i < M; i++) {
        if (request[i] > Available[i]) {
            printf("错误：进程 %d 请求的资源不足！\n", process_id);
            return false;
        }
    }

    // 临时分配资源并更新矩阵
    for (int i = 0; i < M; i++) {
        Available[i] -= request[i];
        Allocation[process_id][i] += request[i];
        Need[process_id][i] -= request[i];
    }

    // 安全性检查
    int safe_sequence[N];  // 安全序列数组
    if (is_safe(safe_sequence)) {
        printf("进程 %d 的资源请求被批准！\n", process_id);
        printf("安全序列: ");
        for (int i = 0; i < N; i++) {
            printf("P%d ", safe_sequence[i]);
        }
        printf("\n");
        return true;
    } else {
        // 如果不安全，则回滚分配
        for (int i = 0; i < M; i++) {
            Available[i] += request[i];
            Allocation[process_id][i] -= request[i];
            Need[process_id][i] += request[i];
        }
        printf("进程 %d 的资源请求被拒绝，系统不安全！\n", process_id);
        return false;
    }
}

int main() {
    // 输入进程数和资源种类数
    printf("请输入进程数 N 和资源种类数 M：");
    scanf("%d %d", &N, &M);

    // 输入可用资源
    printf("请输入系统中各类资源的可用数量：\n");
    for (int i = 0; i < M; i++) {
        scanf("%d", &Available[i]);
    }

    // 输入每个进程的最大资源需求
    printf("请输入每个进程的最大资源需求（Max矩阵）：\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            scanf("%d", &Max[i][j]);
        }
    }

    // 输入每个进程已分配的资源
    printf("请输入每个进程已分配的资源（Allocation矩阵）：\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            scanf("%d", &Allocation[i][j]);
        }
    }

    // 计算需求矩阵 Need
    calculate_need();

    // 打印初始系统状态
    print_system_state();

    // 假设进程 P1 请求资源
    int request[M];
    printf("\n请输入进程 P1 的资源请求：\n");
    for (int i = 0; i < M; i++) {
        scanf("%d", &request[i]);
    }

    // 申请资源并判断是否安全
    request_resources(1, request);

    // 打印系统状态
    print_system_state();

    return 0;
}
