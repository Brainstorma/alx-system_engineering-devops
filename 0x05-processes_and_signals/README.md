# 0x05. Processes and Signals

This repo contains all the tasks that are related to processes and signals. It covers the concepts related to process scheduling, process management, system resources, and process control.

## Table of Contents

- [What is a Process?](#what-is-a-process)
- [Process Creation and Termination](#process-creation-and-termination)
- [Scheduling and Dispatching](#scheduling-and-dispatching)
- [Signals](#signals)
- [Resource Management](#resource-management)
- [Repo Tasks](#repo-tasks)

## What is a Process?

A process is the basic unit of execution in an operating system. It represents a program in execution and can be thought of as the active part of a program. It is the instance of a computer program that is being executed by one or many threads. A process is created by the operating system when a program is executed.

## Process Creation and Termination

Process creation occurs when a program is executed by the operating system. The operating system creates an address space for the process, assigns resources to the process, and schedules the process for execution. The process is then loaded into memory and execution begins. 

Process termination occurs when the process completes its execution or is terminated by the operating system. When a process terminates, it returns all allocated resources to the operating system and releases its address space.

## Scheduling and Dispatching

Process scheduling is the task of the operating system to determine which process to execute at a given time. The scheduling algorithm determines how access to the CPU is managed among competing processes. Scheduling algorithms can be preemptive or non-preemptive, and scheduling decisions are based on priorities and resource availability. 

Process dispatching is the process of executing a process by the operating system. The dispatching decision is made by the scheduler and the process is transferred from the ready queue to the CPU. The process is then executed until a process switch is requested by the operating system.

## Signals

Signals are used by the operating system to notify processes of events. Signals can be sent to processes by the operating system, by another process, or even by the user. 

When a signal is sent to a process, the process is notified of the signal and can take action based on the signal. The action can be to ignore the signal, to terminate the process, or to take some other action.

## Resource Management

Resource management is the task of the operating system to manage the resources of a system. The operating system must manage the resources effectively and efficiently in order to meet the needs of the processes. The resources managed by the operating system include memory, files, I/O devices, processors, and other system resources.

## Repo Tasks

The following tasks are included in this repo:

| Task | Description |
|------|-------------|
| 0-what-is-my-pid | Write a Bash script that displays its own PID. |
| 1-list_your_processes | Write a Bash script that displays a list of currently running processes. |
| 2-show_your_bash_pid | Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process. |
| 3-show_your_bash_pid_made_easy | Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash. |
| 4-to_infinity_and_beyond | Write a Bash script that displays To infinity and beyond indefinitely. |
| 5-kill_me_now | We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.  Write a Bash script that kills 4-to_infinity_and_beyond process. |
| 6-kill_me_now_made_easy | Write a Bash script that kills 4-to_infinity_and_beyond process. |
| 7-highlander | Write a Bash script that displays:  _"To live, you must kill"_  when the  _4-to_infinity_and_beyond_  process is killed. |
| 8-beheaded_process | Write a Bash script that kills the process 7-highlander. |
