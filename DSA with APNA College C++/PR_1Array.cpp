#include <iostream>
using namespace std;


// FInd the smallest and largest number in an Array 
//FOR SMALLEST VALUE IN ARRAY : 
int Smallest(int marks[5]){ 
  int smallest = marks[0];
  for (int i=0 ; i<5 ; i++){ 
     if (marks[i] < smallest){
            smallest = marks[i];
     }
  }
   // FOR INDEX : 
  for (int i=0 ; i<5 ; i++){ 
    if (smallest == marks[i]){ 
        cout << endl << "INDEX IS " << i  << endl ; 
    }
  }
    return smallest ;
}
//FOR LARGEST VALUE IN ARRAY :
int Largest(int marks[5]){
int largest = marks[0];
for (int i = 0 ; i< 5 ; i++){ 
    if (marks[i]>largest){ 
        largest = marks[i];
    }
}
return largest ;
}


int main(){ 
int marks[5] = {1,2,3,-4,5};
int size = sizeof(marks) / sizeof(int);
cout <<"Smallest Number in Marks Is: " << Smallest(marks)<< endl; 
cout <<"Largest Number in Marks Is: " << Largest(marks) << endl ; 

   return 0 ; 
}