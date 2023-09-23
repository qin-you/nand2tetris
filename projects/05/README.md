

## Memory
1. 
```
RAM      000 0000 0000 0000 ~ 0111 1111 1111 1111 111    size:16k    startaddr:0     maxaddr: 16k-1

Screen   100 0000 0000 0000 ~ 1011 1111 1111 1111 111    size:8k     startaddr:16k   maxaddr:24k-1

KBD      110 0000 0000 0000      size:1  startaddr:24k   maxaddr:24k
```

注意到上述地址信息，可用四路解复用，高位 00 01表RAM   10表屏幕   11表键盘

注意测试是有键盘交互的，也有屏幕显示，注意测试界面下方显示。测试前把仿真器View调至Screen模式。


2. 用到的Screen、Keyboard芯片，在tools/builtInChips/下可以找到声明，具体实现是二进制。



## cpu
1. 参照这个接线图（网图，书上也有），把导线接起来，顺序不影响，图中省略了c(控制位)的获取方式，大多数是需要根据指令特定位得到。
![pic](https://pic4.zhimg.com/80/v2-95d7dc5cb51b995e4b40f4d1a202b97f_1440w.webp)

本实验采用的顺序是从左至右、从上到下的顺序连线搭电路。


2. 只看书还不够，书上没找到指令具体到各bit的含义，用到的有：
   1. instruction[6..11]  分别表示ALU的6个控制位：zx nx zy ny f no
   2. [5]: save ALU's out to A-Reg
   3. [12]: means if input is M
   4. [3]: save ALU's out to M
   5. [4]: if outALU's dest is D


3. ARegister DRegister 支持GUI功能，可以用这两个不用之前的Register芯片，用法相同。

4. 一定注意cpu芯片输出引脚pc是小写，且是15位！！！




## Computer
1. 参照下图，按照从左至右顺序搭电路即可。
![](https://pic4.zhimg.com/80/v2-4c2e40edde93106ab31a069e2ad6662f_1440w.webp)

值得说明的是，图中的Memory是包含IO内存的，不只是RAM。 至此，我们实现了冯诺依曼结构理论的一个实际计算机！！！


2. 用到的ROM32K芯片是内置的

3. 本实验的测试文件有多个，都应一一测试。