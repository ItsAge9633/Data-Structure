#include<iostream>
using namespace std;
struct piz
{  int ono,ot;
};

class queue
{  piz p[10];
    int count,c,rear,front,f;
    public:
    queue()
    { c=0;     f=0;  count=0;   front=0; rear=-1;}
       void insert();
       void display();
       void del();
};
void queue::insert()
{     int i=0,n;
       
       cout<<"\n|1. corn pizza";
       cout<<"\n|2. pizza\t\t|";
       cout<<"\n|3. chicken pizza\t|";
      
      
       cout<<"\n        how many order you want to place";
       cout<<"\n---------------------------------------------------------------------";
       cin>>n;
      
      for(i=0;i<n;i++)
       {    if(count>=10)
             {    cout<<"\n____________";
                   cout<<"\n|over flow|";
                   cout<<"\n|__________|";  break;
             }
             else
             {
             c++;
                
            if(rear==9)
            { rear=0;     }
            else
             { rear++;    }
            
             cout<<"\nenter your order";
             cin>>p[rear].ot;
             p[rear].ono=c;      count++; 
             }
       }  
       
}
void queue::display()
{   int i=0,n,f=front; 
    
      cout<<"\n       how many order you want to display";
      cout<<"\n-------------------------------------------------------------------";
      cin>>n;
      for(i=0;i<n;i++)
      {   if(i>=count)
           {    cout<<"\nall data dispalyed";    break;  }
           else
           {
           cout<<"\n____________________________________________";
           cout<<"\nreceive your order please ,no. ->"<<p[f].ono;
           cout<<"\nwhich is:";
           if(p[f].ot==1)
           {     cout<<" corn pizza";   }
            if(p[f].ot==2)
           {     cout<<"  pizza";   }
             if(p[f].ot==3)
           {     cout<<" chicken pizza";   }
           cout<<"\n____________________________________________";
           f++;  
            if(f==10)
            {   f=0;   }      
            }
        }    
}
void queue::del()
{   int i=0,n;
       cout<<"\n-------------------------------------------------------------------"; 
      cout<<"\n       how many order you want to delete";
       cout<<"\n-------------------------------------------------------------------";
      cin>>n;
      for(i=0;i<n;i++)
      {   if(count==0)
           {    cout<<"\nunderflow";    break;  }
           else
           {
           cout<<"\n___________________________";
           cout<<"\ndeleted order no."<<p[front].ono;
           cout<<"\n which is:";
           if(p[front].ot==1)
           {     cout<<"   corn pizza      ";   }
            if(p[front].ot==2)
           {     cout<<"   pizza                ";   }
             if(p[front].ot==3)
           {     cout<<"  chicken pizza";   }
           cout<<"\n___________________________";
          p[front].ono=0;    p[front].ot=0;
          front++;  
          
            if(front==10)
            {   front=0;   }       count--;
            }
        }
          
}
int main()
{  queue q;  int y=1,x;
   while(y==1)
   {    
          cout<<"\n|enter the choice   ";
          cout<<"\n|1.to place order    ";
          cout<<"\n|2.to display order|";
          cout<<"\n|3.to delete order |";
          cout<<"\n|4.to exit                      ";

          cin>>x;
          switch(x)
          {  case 1: q.insert();
                break;
               case 2: q.display();
                break;
                case 3:  q.del();
                break;
               case 4:   y=0;
               break;
               default:   cout<<"\n unknown entry";              
            }
     }                                          

    return 0;
}
