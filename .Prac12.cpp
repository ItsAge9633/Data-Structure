#include <iostream>
using namespace std;
int deque[5], size = 5, f = - 1, r = - 1, val;

//Insert elemnet at front in dequeue
void insert_front()    
{    
    if((f==0 && r==size-1) || (f==r+1))    
    {    
        cout<<"""Queue Overflow"<<endl;    
    }    
    
    else if((f==-1) && (r==-1))    
    {    
        f=r=0;      
    }    
    else if(f==0)    
    {    
        f=size-1;     
    }    
    else    
    {    
        f=f-1;       
    } 
	cout<<"Enter an elemnet to insert in the queue : "<<endl;
    cin>>val;
    deque[f] = val;   
} 

//Insert elemnet at end in dequeue
void insert_rear()    
{    
    if((f==0 && r==size-1) || (f==r+1))    
    {    
        cout<<"""Queue Overflow"; 
    }    
    else if((f==-1) && (r==-1))    
    {    
        r=0;      
    }    
    else if(r==size-1)    
    {    
        r=0;      
    }    
    else    
    {    
        r++;      
    }    
	cout<<"Enter an elemnet to insert in the queue : "<<endl;
    cin>>val;
    deque[r] = val;      
}   

//Delete an elemnet from front
void delete_front()    
{    
    if((f==-1) && (r==-1))    
    {    
        cout<<"Deque is empty";    
    }    
    else if(f==r)    
    {    
        cout<<"The deleted element is "<<deque[f];    
        f=-1;    
        r=-1;    
            
    }    
     else if(f==(size-1))    
     {    
         cout<<"The deleted element is "<<deque[f];  
         f=0;    
     }    
     else    
     {    
          cout<<"The deleted element is "<<deque[f];   
          f=f+1;    
     }    
} 

void delete_rear()    
{    
    if((f==-1) && (r==-1))    
    {    
        cout<<"Deque is empty";    
    }    
    else if(f==r)    
    {    
         cout<<"The deleted element is "<<deque[r];     
        f=-1;    
        r=-1;    
            
    }    
     else if(r==0)    
     {    
         cout<<"The deleted element is "<<deque[r];     
         r=size-1;    
     }    
     else    
     {    
         cout<<"The deleted element is "<<deque[r];     
          r=r-1;    
     }    
} 

void display()    
{    
    int i=f; 
	 if((f==-1) && (r==-1))    
    {    
        cout<<"""Deque is empty";    
    }  
	else{
	printf("\nElements in a deque are: ");           
    while(i!=r){	
    cout<<deque[i]<<" ";
    i=(i+1)%size;
	
    }
   }       
   cout<<deque[r]<<endl;
   
}           





   

int main()    
{    
   cout<<"Which operation want to perfrom"<<endl;
   int ch;
   cout<<"1) Insert element at front in queue"<<endl;
   cout<<"2) Insert element at ent in queue"<<endl;
   cout<<"3) Delete element at fron from queue"<<endl;
   cout<<"4) Delete element at end from queue"<<endl;
   cout<<"5) Display all the elements of queue"<<endl;
   cout<<"6) Exit"<<endl;
   do {
      cout<<"Enter your choice : "<<endl;
      cin>>ch;
      switch (ch) {
         case 1: insert_front();
         break;
         case 2:  insert_rear(); 
         break;
         case 3: delete_front(); 
         break;
         case 4: delete_rear(); 
         break;
         case 5: display(); 
         break;
         case 6: cout<<"Exit"<<endl;
         break;
         default: cout<<"Invalid choice"<<endl;
      }
   } while(ch!=6);
   return 0;  
}     
