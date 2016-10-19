#include <iostream>
#include <cmath>
#include <cstdlib>
#include <list>
#include <fstream>
#include <climits>
long long int neighbours(std::list<long long int>& neigh)
{
    long long int sum_dist = 0;
    long long int top = neigh.front();
    for (std::list<long long int>::iterator i = ++neigh.begin(); 
            i != neigh.end(); i++) {
        sum_dist += abs(top-*i);
    }
    return sum_dist;
}
int main(int argc, const char *argv[])
{
    std::ifstream fin("input.in", std::ios_base::in);
    if (!fin){
        std::cerr << "check your file location ! " << std::endl;
        exit(1);
    }
    
    long long int maxindex = 0;
    long long int tmpindex = 0;
    long long int max  = LLONG_MIN;
    while(fin)
    {
        std::list<long long int> tenmemb;
        for (int i = 0; i < 11; i++) 
        {
            long long int tmp;
            fin >> tmp;
            tenmemb.push_back(tmp);
        }
        long long int tmp = neighbours(tenmemb);
        if (tmp > max) {
            max = tmp;
            maxindex = tmpindex;
        }
        tmpindex++;
    }
    std::cout << max << "\t" << maxindex << std::endl ;
    fin.close();
    return 0;
}
