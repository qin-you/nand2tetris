
## Intro
计算机是一个复杂的系统，对其的教程往往是自顶向下的，这样能够产生较全局的认识。《计算机系统要素》一书，自底向上地，从与非门开始，一步一步实现一个计算机。\
虽是在仿真系统里没有现实硬件，但不乏硬件操作，使用HDL搭电路让人想起当年在面包板上搭一位CPU的实验。软件层面，实现了Hack汇编编译器，VM层，高级语言层和操作系统层。


## Platform
可以选windows可以选linux，我用的windows，需要安装java，仿真环境用java写的。


## Contents
projects/下每个目录都对应一个章节的lab，里面有个README是我做lab时的一点记录。
tools/下是官方提供的工具


## Labs Review
- Project 01:  **Boolean Logic** \
[README](./projects/01/README) \
使用HDL（Hardware Description Language）语言，从与非门开始，搭建与、或、非、 异或、 复用、 多位复用、多路复用、多位多路复用、解复用、多路解复用等电路芯片。

- Project 02: **Boolean Arithmetic** \
[README](./projects/02/README) \
 本lab需实现ALU（Arithmetic Logical Unit），算术逻辑单元，是CPU核心组件。\
 使用HDL语言，基于上个实验创建的电路，依次搭建半加器、全加器、16位加法、16位自增、ALU单元电路芯片。

- Project 03: **Sequential Logic** \
[README](./projects/03/README) \
需要了解数据触发器（DFF）原理、寄存器电路、RAM实现原理。\
先通过DFF实现一个一位寄存器，再实现16位的正常的寄存器，再实现RAM电路（寄存器阵列）。 最大需要实现16K个寄存器的RAM，即32KB大小。


- Project 04: **Machine Language** \
[README](./projects/04/README) \
初探Hack汇编，使用这个特殊的语言编写一个乘法程序和一个键盘读取和屏幕控制的程序。\
Hack汇编只有两类指令：A指令和C指令，其二进制级表示后续会用到。\
README中提供了第二个程序的类C伪代码。

- Project 05: **Computer Archtecture** \
[README](./projects/05/README.md) \
任务是搭建三个芯片的电路:
  * Memory chip：包含RAM部分和I/O内存部分
  * CPU chip：电路图见书上或者README，核心是ALU
  * Computer chip：冯诺依曼体系结构的计算机，由ROM CPU Memory I/O组成 

  ROM芯片已经实现，在 `Tools/buildInChips/ROM32K.hdl`，看不到具体实现，可以看到调用接口。
  
  这个实验应该是最有成就感的一个实验，**从硬件看，至此已经从与非门电路，得到了一个冯诺依曼结构的计算机**。


- Project 06: **Assembler** \
[README](./projects/06/README) \
硬件只认识机器码，为了打通软硬件桥梁，需要写一个编译器，用于将汇编语句编译成二进制码。\
使用python实现的，详见README和assembler.py \
**至此，从软件到硬件打通了，可以使用汇编编写各种程序**，本实验中有Pong游戏可运行测试。


- Project 07: **Virtual Machine I:Stack Arithmetic** \
[README](./projects/07/README) \
往后是虚拟机、高级语言和其编译器的部分。\
虚拟机是高级语言到机器语言（汇编） 的一层中间代码。 加个中间层可以极大提升在不同平台的可移植性。\



## Resource
- 《计算机系统要素》（必须）
- vscode有nand2tetris插件，代码补全很方便（建议）
- 课程视频 （可选）

