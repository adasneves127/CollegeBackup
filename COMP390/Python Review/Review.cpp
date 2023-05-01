#include <iostream>
#include <string>

int main(int argc, char** argv){

    //Store a string with my name
    std::string myName = "Brandon";

    //Store an integer
    int number = 234;

    //Print out my name
    std::cout << myName << "\n";

    //Print out my number
    std::cout << number << " " << myName << "\n";


    //An alternative to python's fstrings
    printf("Hello, my name is %s\n", myName.c_str());
    printf("The answer is %d\n", 3+5);

    printf("character: %s\n", myName.substr(2, 3).c_str());
    printf("character: %s\n", myName.substr(2).c_str());
    printf("character: %s\n", myName.substr(0, 5).c_str());

    // For loop. Iteration on i, from 0 to 10.
    for(int i = 0; i < 10; i++){
        printf("%d ", i);
    }
    printf("\n");

    int i = 0;
    while(i < 10){
        printf("%d\n", i++);
    }

    return EXIT_SUCCESS;
}