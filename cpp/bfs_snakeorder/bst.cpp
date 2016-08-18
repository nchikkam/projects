#include <iostream>

using namespace std;

struct node{
  int n;
  struct node* left;
  struct node* right;
};

node* insert(node* root, int key);
void inorder(node* root);
void levelOrder(node*);
void customOrder(node*);

int main(){
    node* root = NULL;
    int n;

    do{
       cout << "Enter Key [-999] to quit:";
       cin >> n;
       if(n != -999){
          root = insert(root, n);
       }
    }while(n != -999);

    cout << "inOrder:\n";
    inorder(root);

    cout << "\nLevel Order:\n";
    levelOrder(root);

    cout << "\nCustom Order:\n";
    customOrder(root);
    cout << "\n";

}

node* insert(node* root, int key){
   if( root == NULL ){
       root = new node;
       root->n = key;
       root->left = root->right = NULL;
   }
   else if( key < root->n ){
       root->left = insert(root->left, key);
   }else{
       root->right = insert(root->right, key);
   }
   return root;
}

void inorder(node* root){
  if(root!= NULL){
     inorder(root->left);
     cout << root->n << " ";
     inorder(root->right);
  }
}

void levelOrder(node* root){
 node* queue[100]; //queue
 int front = 0;
 int rear = 0;
 if( root == NULL ) return;
 queue[rear++] = root;
 while(front!=rear){
    node* tmp =  queue[front++];
    cout << tmp->n << " ";
    if( tmp->left != NULL)
        queue[rear++] = tmp->left;
    if( tmp->right != NULL )
        queue[rear++] = tmp->right;
 }
}

void customOrder(node* root){
     node* p_queue[100]; //queue
     node* c_queue[100];

     int p_front = 0;
     int c_front = 0;
     int p_rear = 0;
     int c_rear = 0;
     int flag = 0; // left to right

     if( root == NULL ) return;
     p_queue[p_rear++] = root;
     cout << " " <<root->n << "\n";
     while(p_front!=p_rear){
        node* tmp =  p_queue[p_front++];
        if( tmp->left != NULL)
            c_queue[c_rear++] = tmp->left;
        if( tmp->right != NULL )
            c_queue[c_rear++] = tmp->right;
        if (p_front == p_rear){
            for(int i=c_front, j=0; i< c_rear; i++, j++){
                p_queue[j] = c_queue[i];
            }
            p_front = 0;
            p_rear = c_rear;

            if (flag){
                flag = 0;
                for(int l = p_rear-1; l >=0; l--){ // print reverse
                    cout<< " "<< p_queue[l]->n;
                }
            }else{
                flag = 1;
                for(int i = 0; i < p_rear; i++)
                    cout << " " << p_queue[i]->n;
            }

            cout << "\n";
            c_front = 0;
            c_rear = c_front;
        }
     }
}
