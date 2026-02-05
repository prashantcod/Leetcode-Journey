#include <iostream>
#include <vector> 
using namespace std ; 


int main(){ 
      vector <int> v;
      // cout << v[0] << " "; 
      // cout << v[1] << " ";
      // cout << v[2] << " ";
      // cout << v[3] << " ";
      // cout << v[4] << " ";
      
      //? Vector push and pop 
      v.push_back(21); 
      v.push_back(34); 
      v.push_back(67); 

      
      // v.pop_back();


     //? FRONT AND BACK VALUES ACCESSING IN VECTOR : 
    //  cout << v.front() << endl; 
    //  cout << v.back() << endl ; 

     //? AT fxn in vector : use to access the value in ith index 
    //  cout << v.at(1) << endl ; 

      //? FOR EACH LOOP IN C++ here the iterator will not save the idx it will have real value 
      for (int value : v){ 
           cout << value << endl ;
      }

      //?size of vector : 
      cout << v.size() << endl ; 

      //? capacity of vector : 
      cout << v.capacity() << endl ; 





  return 0 ; 
}