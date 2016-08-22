#include <iostream>
#include <vector>
#include <map>
#include <stdlib.h>

#include <assert.h>

using namespace std;

// A data source to provide sample data to the demo version of this program.
// This holds a map like structure and acts as an external source of data that
// the cache need to update from in case of a MISS event.
class UserDataInMemory{
public:
    map<string, string> userData;               // map

    UserDataInMemory(){
        userData["userId-1"] = "userNameOne";
        userData["userId-2"] = "userNameTwo";
        userData["userId-3"] = "userNameThree";
        userData["userId-4"] = "userNameFour";
        userData["userId-5"] = "userNameFive";
    }

    ~UserDataInMemory(){
        userData.clear();
    }

    map<string, string> & getUserData(){        // exposes the data for consumer cache
        return userData;
    }

    string getUserByID(string userID){          // does a lookup on map, writes and error in case of miss
        cout << "getUserByID(...) Called.\n";
        if (userData.count(userID) == 1){
            return userData[userID];
        }else{
            cout << "ERROR: BAD USER ID: Requested Key Not Found in Memory";
            return "";
        }
    }

};

// A basic Entry class that the class keeps a table of. In order to keep the design
// simple and loosely coupled, individual classes are created and Entry is one of them
// This is just like the definition of a Node in a Doubly Linked List, but with pair data
// that forms the <key, value> pair in each node with each node pointing to the node
// previous to it and node next to it. - A self referential structure :)
template<class Key, class Value>
struct Entry {
	Key     key;
	Value   data;
	Entry*  prev;
	Entry*  next;
};

// This class holds the minimal and simple implementation of a Doubly Linked List.
// The Idea of this class in Cache design was to make the :
// 1. Cache reorganization fast
// 2. Keep the order of the items accessed in an easily accessible and changeable format.
// 3. To support removal of an entry from Cache in O(1) time complexity.
// 4. To support addition of an entry in O(1)
// The class also exposes a print(...) method which could be useful for further enhancements.
template<class Key, class Value>
class DList{
public:
    Entry<Key, Value> *head, *tail;     // a Queue needs 2 pointers, one where to insert, (tail)
                                        // another where to delete (head) FIFO
    unsigned count, capacity;           // count to keep the no of nodes in the list.
                                        // when capacity reaches count, list needs organization for
                                        // further inserts.

    DList(unsigned nodeCount){
        capacity = nodeCount;
        head = new Entry<Key,Value>;
		tail = new Entry<Key,Value>;
		head->prev = NULL;
		head->next = tail;
		tail->next = NULL;
		tail->prev = head;
    }

    ~DList(){
        while(head!=NULL){                      // logic of clearing a DList
            Entry<Key,Value>* temp = head;
            head=head->next;
            delete temp;
        }
    }

	void remove(Entry<Key,Value>* node) {       // beauty of removal in O(1)
		node->prev->next = node->next;
		node->next->prev = node->prev;
		count -= 1;
	}
	void addInFront(Entry<Key,Value>* node) {
		node->next = head->next;
		node->prev = head;
		head->next = node;
		node->next->prev = node;
		count+=1;
	}
	void print(){
	    Entry<Key,Value>* temp = head;
	    while(temp!=NULL){
            cout << "{"<<temp->key << ","<<temp-> data << "}, ";
            temp=temp->next;
        }
        cout << endl;
	}
};

// The main driver class for this program. This class holds the below compositions:
// 1. Table [hash] to keep the items that have been requested for faster access for
//    further lookups
// 2. A Doubly Linked List class to keep track of the items looked up. The Idea of
//    this class address the question: 'What if the Cache is Full and Which Element
//    must be removed to create space for New One'. Well, the List is smart enough
//    to keep the FIFO order so that there is a way to delete a lookup entry that was
//    looked up long time ago.
template<class Key, class Value>
class Cache
{
private:
	map<Key, Entry<Key,Value>* >	hash;           // the Main Look Up Table for Cache
	DList<Key,Value> *entries;                      // Doubly LList
	UserDataInMemory externalData;                  // A Sample Data Source for Demoing application

public:
	Cache(unsigned int capacity) {
		entries = new DList<Key,Value>(capacity);
	}

	~Cache() {
		delete entries;
	}

	// indicates if the cache reached to the limit
    bool cacheFull(){
        //return (entries->count == entries->capacity);
        cout << "hash::size: "<<hash.size() << endl;
        cout << "capacity:   "<<entries->capacity << endl;
        return hash.size() >= entries->capacity;
    }

    void prnt(){
        for(map<string, Entry<string,string>* >::const_iterator it = hash.begin();
        it != hash.end(); ++it)
        {
            std::cout << it->first << "\n";
        }
    }

    // This method gets called when ever there was a MISS or Cache need
    // to be reorganized in case if it reached to its capacity to hold entries.
	void set(Key key, Value data)
	{
	    Entry<Key,Value>* node = hash[key];
		if(node) {
			// refresh the link list
			entries->remove(node);
			node->data = data;
			entries->addInFront(node);
		}
		else{
			if ( cacheFull() ){
			    node = entries->tail->prev;
			    entries->remove(node);
			    hash.erase(node->key);
			    node->key = key;
			    node->data = data;
			    hash[key] = node;
			    entries->addInFront(node);
			}
			else{
                node = new Entry<Key,Value>;
                node->key = key;
                node->data = data;
                hash[key] = node;
                entries->addInFront(node);
			}
		}
	}

	// It does the respective part. It checks if the requested key is in the
	// cache lookup table, if it finds, which is a HIT, it returns the userName
	// if it was a MISS, it gets the data from the external data source which
	// could be a database or file in real time, but an In Memory map in our case
	// and updates the map with set method.
	Value get(Key key) {
	    prnt();
	    if(hash.count(key)==1) {
            Entry<Key,Value>* node = hash[key];
            cout << "<HIT>  --> requested UserID found in Cache.";
			entries->remove(node);
			entries->addInFront(node);
			return node->data;
		}
		else{
            // not found in cache, read from external source and create entry
            cout << "<MISS>  --> UserID not found in Cache, Reading from Memory\n";
            string userName = externalData.getUserByID(key);
            if (userName.length() > 0){
                set(key, userName);
            }
            return userName;
		}
	}

    // helper to print the cache
	void print(){
        entries->print();
	}
};


void demoOne(){
    unsigned cacheSize = 20;
    Cache<string, string> cache(cacheSize);

    cache.print();

    UserDataInMemory userData;

    for(map<string, string>::iterator it = userData.getUserData().begin();
        it != userData.getUserData().end();
        ++it) {
            cache.get((it->first) );
            cache.print();
    }

    for(map<string, string>::iterator it = userData.getUserData().begin();
        it != userData.getUserData().end();
        ++it) {
            cache.get((it->first) );
            cache.print();
    }
}

// Demo Two
void demoBadUserID(){
    unsigned cacheSize = 20;
    Cache<string, string> cache(cacheSize);

    cache.print();
    cache.get("BADUSERID");
}

// sample demos for testing
void demos(){
    demoOne();
    demoBadUserID();
}

// Main drive method that invokes the application and generates the report
// with the help of classes.
int main (int argc, char *argv[]){
    unsigned cacheSize;


    if(argc == 2){  // all params mentioned
        cacheSize = atoi(argv[1]);
        Cache<string, string> cache(cacheSize);
        string userID;
        string choice;

        do{
            cout <<  "Cache Entries: ";
            cache.print();
            cout << "Enter UserID to LookUp:" ;
            cin >> userID;
            cache.get(userID);
            cout << "\nContinue with Another Lookup ? [Y/N]: ";
            cin >> choice;
        }while(choice.c_str()[0]== 'Y' || choice.c_str()[0]== 'y' );

    }else {  // usage
        cout<<"usage: "<< argv[0] <<" <capacity>";
        exit(0);
    }
    return 0;
}
