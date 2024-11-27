#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

#define getpch(type) (type *)malloc(sizeof(type))

int t = 0;  // 记录时间片
struct pcb {  // 定义进程控制块PCB
    char name[10];  // 进程名
    char state;     // W/R/F (等待/运行/完成)
    int super;      // 优先数
    int ntime;      // 总运行时间
    int rtime;      // 已耗时
    struct pcb* link;  // 指向下一个进程
} *ready = NULL, *p;
typedef struct pcb PCB;

// 排序函数，按照优先数从高到低排序，同优先级先来先服务
void sort() {
    p->link = NULL;
    if (ready == NULL)
        ready = p;
    else {
        if (p->super > ready->super) {  // 如果当前进程的优先数比队列中的第一个进程高
            p->link = ready;
            ready = p;
        }
        else {
            PCB* f = ready;
            while (1) {
                if (f->link == NULL) {  // 如果是最后一个进程
                    f->link = p;
                    return;
                }
                else if (p->super > f->link->super) {  // 如果当前进程的优先数比下一个进程的优先数高
                    PCB* s = f->link;
                    f->link = p;
                    p->link = s;
                    return;
                }
                f = f->link;
            }
        }
    }
}

// 输入进程信息
void input() {
    srand((unsigned)time(NULL));
    int n;
    cout << "请输入进程数目：";
    cin >> n;
    for (int i = 0; i < n; i++) {
        p = getpch(PCB);
        cout << "请分别输入进程名、进程优先数、运行时间：";
        cin >> p->name >> p->super >> p->ntime;
        
        p->state = 'W';
        p->rtime = 0;
        sort();
    }
}

// 显示进程信息
void disp(PCB* pr) {
    cout << "进程名：" << pr->name << "  ";
    cout << "进程状态：" << (pr->state == 'W' ? "就绪" : (pr->state == 'R' ? "运行" : "完成")) << "  ";
    cout << "进程总运行时间：" << pr->ntime << "  ";
    cout << "进程剩余运行时间：" << (pr->ntime - pr->rtime) << "  ";
    cout << "进程已经消耗时间：" << pr->rtime << endl;
}

// 查看当前进程和就绪队列
void check() {
    cout << "-------------------" << " 正在运行中的进程 " << "------------------------------" << endl;
    disp(p);
    cout << "-------------------" << " 就绪队列中的进程 " << "------------------------------" << endl;
    PCB* pr = ready;
    while (pr != NULL) {
        disp(pr);
        pr = pr->link;
    }
}

// 销毁已完成的进程
void destroy() {
    cout << "进程" << p->name << "运行完成，耗时" << p->ntime << "个CPU时间片" << endl;
    free(p);
    p = NULL;
}

// 进程就绪函数
void running() {
    p = ready;
    ready = ready->link;
    t++;
    cout << endl << "这是第" << t << "个CPU时间片" << endl;
    p->state = 'R';
    check();
    p->rtime++;
    if (p->ntime == p->rtime) {
        destroy();
    }
    else {
        p->super -= 1;  // 优先数减 1
        p->state = 'W';
        sort();  // 重新排序
    }
    if (p == NULL && ready == NULL)
        cout << "全部完成，共耗时" << t << "个CPU时间片" << endl;
}

// 主函数
int main() {
    input();  // 输入进程信息
    while (p != NULL || ready != NULL)  // 循环直到所有进程都完成
        running();
    return 0;
}
