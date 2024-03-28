#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<ctime>
#include<random>

#define ville 5

std::vector<int> ginitial(){
    std::vector<int> x;
    for(int i = 0; i < ville; i++)
        x.push_back(i);
    std::shuffle(x.begin(), x.end(), std::mt19937(std::random_device()()));
    return x;
}

std::vector<std::vector<int>> echange(std::vector<int> x){
    std::vector<int> neighbor = x;
    std::vector<std::vector<int>> Allmove;
    for(int i = 0; i < ville-1; i++){
        for(int j = i+1; j < ville; j++){
            neighbor = x;
            std::swap(neighbor[i], neighbor[j]);
            Allmove.push_back(neighbor);
        }
    }
    return Allmove;
}

std::vector<std::vector<int>> inversion(std::vector<int> x){
    std::vector<int> neighbor = x;
    std::vector<std::vector<int>> Allmove;
    for(int i = 0; i < ville; i++){
        neighbor = x;
        std::swap(neighbor[i], neighbor[i+1]);
        Allmove.push_back(neighbor);
    }
    return Allmove;
}

std::vector<std::vector<int>> deplacement(std::vector<int> x){
    std::vector<int> neighbor = x;
    std::vector<std::vector<int>> Allmove;
    for(int i = 0; i < ville-1; i++){
        for(int j=i+1; j < ville; j++){
            neighbor = x;
            std::swap(neighbor[i], neighbor[j+1]);
            std::swap(neighbor[j], neighbor[j+1]);
            Allmove.push_back(neighbor);
        }
    }
    return Allmove;
}
int main(){
    std::vector<int> x = ginitial();
    std::vector<std::vector<int>> Allmove = deplacement(x);
    for(int i = 0; i < Allmove.size(); i++){
        for(int j = 0; j < Allmove[i].size(); j++){
            std::cout << Allmove[i][j] << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}