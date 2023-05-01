#include <string>
#include <stdint.h>
#include <iostream>
#include <vector>

class Character{
    public:
        Character();
        void print();
        void changeHp(int change);  
    private:
        std::string npcType;
        uint32_t hp;
        std::string weapon;
        std::vector<std::string> drop;
        float defenceFactor;  
};