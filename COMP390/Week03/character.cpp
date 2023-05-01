#include "character.h"

Character::Character(){
    this->npcType = "Monster";
    this->hp = 100;
    this->weapon = "Sword";
    this->drop.push_back("Red_Gem");
    this->drop.push_back("Gold_Coin");
    this->defenceFactor = 0.345;
}

void Character::print(){
    std::cout << "Npc type: " << npcType << std::endl;
    std::cout << "Hp: " << hp << std::endl;
    std::cout << "Weapon: " << weapon << std::endl;
    std::cout << "Drop: " << drop[0] << std::endl;
    std::cout << "Drop2: " << drop[1] << std::endl;
    std::cout << "Defence factor: " << defenceFactor << std::endl;
}

void Character::changeHp(int change){
    hp += change;
}