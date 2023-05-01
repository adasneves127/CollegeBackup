#pragma region Includes
    #include <iostream>
    #include <string>
    #include <stdint.h>
    #include <vector>
    #include <unistd.h>
    #include <map>
    #include "character.h"
    //#include <stdio.h>
#pragma endregion

#pragma region Poision
//This is a region that is used to 'poison' the code, that is to say, make certain functions cause errors if they are used.
    #pragma GCC poison sprintf fprintf
#pragma endregion

#pragma region Function Prototypes
#pragma endregion

#pragma region Global Variables
#pragma endregion

#pragma region Classes

class Npc{
    public:
        Npc(std::string npc_type, uint32_t hp, std::string weapon, std::string drop, std::string drop2, float defence_factor){
            this->npc_type = npc_type;
            this->hp = hp;
            this->weapon = weapon;
            this->drop = drop;
            this->drop2 = drop2;
            this->defence_factor = defence_factor;
        }
        void print(){
            std::cout << "Npc type: " << npc_type << std::endl;
            std::cout << "Hp: " << hp << std::endl;
            std::cout << "Weapon: " << weapon << std::endl;
            std::cout << "Drop: " << drop << std::endl;
            std::cout << "Drop2: " << drop2 << std::endl;
            std::cout << "Defence factor: " << defence_factor << std::endl;
        }
        void changeHealth(int change){
            hp += change;
        }
    private:
        std::string npc_type;
        uint32_t hp;
        std::string weapon;
        std::string drop;
        std::string drop2;
        float defence_factor;
};

#pragma endregion

int main(void){
    std::vector<int> myList;
    myList.push_back(2);
    myList.push_back(6);
    myList.push_back(5);
    myList.push_back(3);
    int firstElement = myList[0];
    std::cout << "This is the list: [";
    for (int i = 0; i < myList.size(); i++){
        std::cout << myList[i];
        if (i != myList.size() - 1){
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;

    std::cout << "This is the first element: " << firstElement << std::endl;

    for(int i = 0; i < myList.size(); i++){
        std::cout << myList[i] << std::endl;
    }

    FILE* file;
    file = fopen("test.txt", "r");
    if(file == NULL){
        std::cout << "Error opening file" << std::endl;
    }
    while(!feof(file)){
        char buffer[256];
        fgets(buffer, sizeof(buffer), file);
        std::cout << buffer;
    }
    sync();
    if(fclose(file) != 0){
        std::cout << "Error closing file" << std::endl;
    } else {
        std::cout << "File closed successfully" << std::endl;
    }

    Character npc1 = Character();
    npc1.print();

    return EXIT_SUCCESS;
}
void printVector(std::vector<int> myList){
    std::cout << "This is the list: [";
    for (int i = 0; i < myList.size(); i++){
        std::cout << myList[i];
        if (i != myList.size() - 1){
            std::cout << ", ";
        }
    }
    std::cout << "]" << std::endl;
}