#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <stdlib.h>
using namespace std;

struct sourceDetails {
    //details of each source such as ID and rectangle coordinates are encapsulated here
    string ID;
    int x,y,w,h;    
} source1,source2;

int randomSourceCountGen() {
    return ((rand()%2) + 1); //generate either one source or two
}

vector<vector<int>> getVectorElements(vector<vector<int>> sourceData,int n,sourceDetails source1, sourceDetails source2) {
    int firstSourceID = stoi(source1.ID);
    int secondSourceID = stoi(source2.ID);
    if(n==1) {
        sourceData[0] = {firstSourceID,source1.x,source1.y,source1.w,source1.h};
    }
    else {
        sourceData[0] = {firstSourceID,source1.x,source1.y,source1.w,source1.h};
        sourceData[1] = {secondSourceID,source2.x,source2.y,source2.w,source2.h};
    }
    return sourceData;
}

sourceDetails getSourceInfo(int n, sourceDetails source1, sourceDetails source2) {
    if(n==1) {
        //number of sources = 1, fill only one source details
        source1 = {"2678499066",15, 0, 1852, 1042};
        source2 = {"0",0,0,0,0}; //not defined
    }
    else {
        //split the window into two approximate halves
        source1 = {"2678499066",0, 252, 960, 540};
        source2 = {"3637328212",960,252,960,540};
    }
    return source1,source2;
}

void printVector(vector<vector<int>> sourceData) {
    for(int i=0;i<sourceData.size();i++) {
        for(int j=0;j<sourceData[i].size();j++) {
            cout<<sourceData[i][j]<<" ";
        }
        cout<<endl;
    }
}

int main() {
    int infoCount = 5;

    int numberOfSources = randomSourceCountGen();
    cout<<"No. of sources: "<<numberOfSources<<endl;
    source1 = {"2674",0,252,960,540};
    cout<<source1.ID<<endl;
    //////
    if(numberOfSources == 1) 
        source1 = {"2674",0,0,1920,1080};

    else {
        
        source1 = {"2674",0,252,960,540};
        source2 = {"3674",960,252,960,540};
    }
    /////
    vector<vector<int>> sourceData(numberOfSources);
    cout<<sourceData.size()<<endl;
    if(numberOfSources==1) 
        sourceData[0] = {stoi(source1.ID),source1.x,source1.y,source1.w,source1.h};
    else {
        sourceData[0] = {stoi(source1.ID),source1.x,source1.y,source1.w,source1.h};
        sourceData[1] = {stoi(source2.ID),source2.x,source2.y,source2.w,source2.h};
    }
    printVector(sourceData);

    return 0;

}