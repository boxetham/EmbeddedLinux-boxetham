// From : http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem
//
// Be sure to set -O3 when compiling.
// Modified by Mark A. Yoder  26-Sept-2013
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
	printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
}

int main(int argc, char *argv[]) {
    volatile void *gpio_addr;
    volatile unsigned int *gpio_oe_addr;
    volatile unsigned int *gpio_setdataout_addr;
    volatile unsigned int *gpio_cleardataout_addr;
    unsigned int reg;
    volatile void *gpio_addr1;
    volatile unsigned int *gpio_oe_addr1;
    volatile unsigned int *gpio_setdataout_addr1;
    volatile unsigned int *gpio_cleardataout_addr1;
    unsigned int reg1;
    volatile void *gpio_addr2;
    volatile unsigned int *gpio_datain;
    volatile unsigned int *gpio_datain1;
    volatile unsigned int *gpio_oe_addr2;
    volatile unsigned int *gpio_setdataout_addr2;
    volatile unsigned int *gpio_cleardataout_addr2;
    unsigned int reg2;
    int LED;
    int LED1;
    int switch1;
    int switch2;
    
    // Set the signal callback for Ctrl-C
	signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    gpio_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO3_START_ADDR);
    gpio_addr1 = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
    gpio_addr2 = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO0_START_ADDR);

    gpio_oe_addr           = gpio_addr + GPIO_OE;
    gpio_setdataout_addr   = gpio_addr + GPIO_SETDATAOUT;
    gpio_cleardataout_addr = gpio_addr + GPIO_CLEARDATAOUT;

    gpio_oe_addr1           = gpio_addr1 + GPIO_OE;
    gpio_datain1            = gpio_addr1 + GPIO_DATAIN;
    gpio_setdataout_addr1   = gpio_addr1 + GPIO_SETDATAOUT;
    gpio_cleardataout_addr1 = gpio_addr1 + GPIO_CLEARDATAOUT;

    gpio_oe_addr2           = gpio_addr2 + GPIO_OE;
    gpio_datain             = gpio_addr2 + GPIO_DATAIN;
    gpio_setdataout_addr2   = gpio_addr2 + GPIO_SETDATAOUT;
    gpio_cleardataout_addr2 = gpio_addr2 + GPIO_CLEARDATAOUT;

    if(gpio_addr == MAP_FAILED || gpio_addr1 == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }

    // Set USR3 to be an output pin
    LED = (1<<21);
    LED1 = (1<<28);
    switch1 = (1<<7);
    switch2 = (1<<17);
    reg = *gpio_oe_addr;
    reg1 = *gpio_oe_addr1;
    printf("GPIO1 configuration: %X\n", reg);
    reg &= ~LED;       // Set USR3 bit to 0
    reg1 &= ~LED1;
    *gpio_oe_addr = reg;
    *gpio_oe_addr1 = reg1;
    printf("GPIO1 configuration: %X\n", reg);

    printf("Start blinking LED USR3\n");
    while(keepgoing) {
        if(*gpio_datain & switch1) {
            *gpio_setdataout_addr1 = LED1;
    	} else {
            *gpio_cleardataout_addr1 = LED1;
    	}

        if(*gpio_datain1 & switch2) {
            *gpio_setdataout_addr= LED;
    	} else {
            *gpio_cleardataout_addr = LED;
    	}
/**
        *gpio_setdataout_addr = LED;
        *gpio_setdataout_addr1 = LED1;

	usleep(250000);

        *gpio_cleardataout_addr = LED;
        *gpio_cleardataout_addr1 = LED1;

	usleep(250000); **/
    }

    munmap((void *)gpio_addr, GPIO1_SIZE);
    munmap((void *)gpio_addr1, GPIO1_SIZE);
    close(fd);
    return 0;
}
