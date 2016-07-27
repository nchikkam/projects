#include <iostream>
#include <fstream>
#include <vector>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>          // for output print

#include <time.h>           // for parsing date
#include <sstream>
#include <algorithm>
#include <string.h>

using std::setw;
using namespace std;

// A simple Date class that encapsulates date(day, month, year) into single
// unit so that  the  management  of  dates become easy in this application
// development.
//
// Overloads the assignment '=' operator so that assigning a date value to
// another becomes easy
// Overloads the extraction operator so that the instance could be serialized
// to a standard output stream, such as cout.
class Date{
private:
    int day, month, year, hours, mins, seconds;
    long timeStamp;
public:
    // ctor
    Date(){}
    // dtor
    virtual ~Date(){}

    // setter and getters
    void setDay(int mday){day = mday;}
    void setMonth(int mnth){month = mnth;}
    void setYear(int yr){year = yr;}
    void setHour(int hour){hours = hour;}
    void setMinutes(int minute){mins= minute;}
    void setSeconds(int second){seconds= second;}

    void setTimeStamp(long ts){timeStamp=ts;}
    int getDay(){return day;}
    int getMonth(){return month;}
    int getYear(){return year;}
    long getTimeStamp(){return timeStamp;}

    // assignment overloading to treat date objects similar to primitive types
    void operator=(const Date &dt ){
        day     = dt.day;
        month   = dt.month;
        year    = dt.year;
        hours   = dt.hours;
        mins    = dt.mins;
        seconds = dt.seconds;
        timeStamp = dt.timeStamp;
    }

    // over loading << operator to stream it to a cout during statment generation
    friend ostream& operator<<(ostream& os, const Date& dt){
        os  << setfill('0') << setw(2) << dt.day    << '/'
            << setfill('0') << setw(2) << dt.month  << '/'
            << setfill('0') << setw(2) << dt.year   << ' '
            << setfill('0') << setw(2) << dt.hours  << ':'
            << setfill('0') << setw(2) << dt.mins   << ':'
            << setfill('0') << setw(2) << dt.seconds;
        os.fill(' ');
        return os;
    }
};

// This class is abstraction of transaction with in the BankAccount system.
// Regular activities on an Account would be crediting, withdrawing and
// generation of details and this class is a unit to represent each transaction.
class Record{
public:
    long        userID;
    string      userName;
    Date        date;               // composition, 'contains' Date as member
    string      description;
    double      amount;

    // Ctor method that accepts an input line, parses it and populates fields
    Record(string line){
        vector<string> fields = split(line, '|');
        this->userID = atol(fields[0].c_str());
        this->userName = fields[1];
        this->description = fields[2];
        this->amount = atof(fields[3].c_str());
        Date date;
        parseDateStringToDateTime(fields[4], date);
        this->date = date;
    }

    // Handy Ctor that could be used when all fields are avalable
    Record(long userId, string userName, string description, double amount, Date date){
        this->userID = userId;
        this->userName = userName;
        this->description = description;
        this->amount = amount;
        this->date = date;
    }

    Date getDate(){
        return this->date;
    }

    // Dtor to cleanup resources after completion of execution.
    virtual ~Record(){
        userName.clear();
        description.clear();
    }

    // A helper method to parse a line with delimited transaction fields.
    // it scans the line for a pipe character in our case, adds them to
    // the vector, returns the vector on reaching the end of the string.
    static std::vector<std::string> split(const std::string &line, char sep) {
      std::vector<std::string> tokens;
      std::size_t start = 0, end = 0;
      while (start < line.length() && (end = line.find(sep, start)) != std::string::npos) {
        tokens.push_back(line.substr(start, end - start));
        start = end + 1;
      }
      return tokens;
    }

    // A helper method to convert given date string into a date instance.
    // For the report generation, this is mandatory as the audience might
    // want the date to be displayed in a different format than a number.
    void parseDateStringToDateTime(string str, Date &date){
        time_t rawtime;
        struct tm * timeinfo;
        int year, month ,day, hour, minutes, seconds;

        char *s = new char[str.length()];
        strcpy(s, str.c_str());

        replace( s, s+strlen(s), '/', ' ' );
        replace( s, s+strlen(s), ':', ' ' );
        istringstream( s ) >> year >> month >> day >> hour >> minutes >> seconds;

        time ( &rawtime );
        timeinfo = localtime ( &rawtime );
        timeinfo->tm_year = year - 1900;
        timeinfo->tm_mon = month - 1;
        timeinfo->tm_mday = day;
        timeinfo->tm_hour = hour;
        timeinfo->tm_min = minutes;
        timeinfo->tm_sec = seconds;

        time_t timestamp;

        timestamp = mktime ( timeinfo );

        date.setDay(day);
        date.setMonth(month);
        date.setYear(year);
        date.setHour(hour);
        date.setMinutes(minutes);
        date.setSeconds(seconds);
        date.setTimeStamp((long)timestamp);
    }

    // Over loading of the << operator so the string representation of
    // this instance can be displayed.
    friend ostream& operator<<(ostream& os, const Record& rec){
        //os  << rec.userName     << setw(20)
        os    << rec.date      << setw(20)
            << rec.description  << setw(30)
            << rec.amount       << setw(30)
            << "\n";
        return os;
    }
};

// This class has got nothing to do with the actual implementation of the
// statement generation. However, this class could be useful for demo purposes.
// It encapsulates the logic of retrieving the transaction records for a user,
// features another API call to get the Opening Balance amount for a user while
// opening his account.
//
// It also exposes a method 'next()' that allows the subscribers of this class to
// iterate through the retrieved records one by one.
class Generator{
private:
    string  transactionsFile,   // a running file that contains all transactions
            masterFile;         // master file that associates userID to userName
    vector<string> lines;       // a container to keep the retrieved records for a user
    unsigned index;             // index pointer to allow next() API to return records
                                // in a sequence
public:
    // ctor, instantiates the dataSources, resets the index counter
    Generator(string txFile, string mstFile):
        transactionsFile(txFile), masterFile(mstFile), index(0) // initialization list
    {
        transactionsFile = txFile;
        masterFile = mstFile;
    }
    virtual ~Generator(){}

    // this method is a helper method and  returns all the valid transactions by a user
    void getTransactionsForUser(long userId){
        ifstream input_file(transactionsFile.c_str());// open file
        if (!input_file.is_open()) {
            cout << "Transactions file could not be opened! Terminating!" << endl;
            throw std::exception();
        }
        string line;
        while (std::getline(input_file, line)){
            if(line.c_str()[0] == '#') continue;  // skip first heading line
            string user;
            stringstream sstream;
            sstream << userId;
            user = sstream.str();

            std::size_t found = line.find(user);
            if (found!=std::string::npos)
                lines.push_back(line);
        }
        input_file.close();
    }

    // this method returns the opening balance
    // Reads the master.txt file and visits each line, if the requested
    // user is found, it returns the opening balance from that line returns
    // 0.0 if user not found.
    double getInitialBalance(long userId){
        ifstream input_file(masterFile.c_str());// open file
        if (!input_file.is_open()) {
            cout << "Master file could not be opened! Terminating!" << endl;
            throw std::exception();
        }
        string line, user;
        stringstream sstream;
        sstream << userId;
        user = sstream.str();

        while (std::getline(input_file, line)){
            if(line.c_str()[0] == '#') continue;  // skip first heading line
            std::size_t found = line.find(user);
            if (found!=std::string::npos){
                vector<string> fields = Record::split(line, '|');
                return atof(fields[2].c_str());
            }
        }
        input_file.close();
        return 0.0;
    }

    // A helper method to retrieve the user name from the master.txt dataSource.
    // this method opens the file, looks for the requested userID while traversing
    // file line by line, when ever it finds the requested user in the line, it
    // reports the userName  by returning it.
    string getUserName(long userId){
        ifstream input_file(masterFile.c_str());// open file
        if (!input_file.is_open()) {
            cout << "Master file could not be opened! Terminating!" << endl;
            throw std::exception();
        }
        string line, user;
        stringstream sstream;
        sstream << userId;
        user = sstream.str();

        while (std::getline(input_file, line)){
            if(line.c_str()[0] == '#') continue;  // skip first heading line
            std::size_t found = line.find(user);
            if (found!=std::string::npos){
                vector<string> fields = Record::split(line, '|');
                return fields[1];
            }
        }
        input_file.close();
        return "";
    }

    // This method simulates the iterator kind of pattern and returns a new
    // line from the container each time its called. If it reaches to the end
    // of the list, it returns "EOF" to indicate it.
    string next(){
        if ( index < lines.size() )
            return lines[index++];
        return "EOF";
    }
};

// Global Assumptions:
string txFile("C:/nary/cpp/src/transactions.txt");  // transaction for all users
string mstFile("C:/nary/cpp/src/master.txt");       // userID to userName association master file
Generator dataSource(txFile, mstFile);           // global object to expose the userData and transactions
                                                 // for monthly statement generation.

// A base class that comprises of the main logic of an Account
// with in a BankAccount System.
//
// it basically wraps userID, Name, OpeningBalance and few constants
// such as penalty and minimum balance limit that are mandatory for
// creating an Account.
class Account{
private:
            long    m_lUserID;                  // unique userID/accountNumber
            string  m_strUserName;              // userName
            double  m_dOpeningBalance;          // initial amount
    const   double  m_ctMinSafeBalanceAmount;   // balance limit to be maintained
    const   double  m_cdPenaltyPercentage;      // penalty in case the balance < limit

public:

    // Ctor to set the initial values, it initialize members and
    // calls global APIs to retrieve user Data and keep them ready
    Account(long userId):
        m_lUserID(userId),
        m_ctMinSafeBalanceAmount(1000),         // best way to initialize member const(s)
        m_cdPenaltyPercentage(10)
    {
        initAccountDetails();
    }

    // populate the userName and opening Balance.
    void initAccountDetails(){
        m_strUserName = dataSource.getUserName(m_lUserID);
        m_dOpeningBalance = dataSource.getInitialBalance(m_lUserID);
    }

    // pure abstract methods to make the instantiation of this class impossible
    // prevent users from instantiating this class.
    virtual ~Account() = 0; // make it pure virtual to make this class abstract
    virtual void generateStatement(int) = 0;
    virtual void setReportFileName(string) = 0;

    // setter and getter helpers
    void setUserID(long userId){m_lUserID = userId;}
    long getUserID(){return m_lUserID;}
    void setUserName(string user){ m_strUserName = user;}
    string getUserName(){return m_strUserName;}
    void setOpeningBalance(double balance){ m_dOpeningBalance = balance;}
    double getOpeningBalance(){return m_dOpeningBalance;}
    double getSafeBalanceLimit(){return m_ctMinSafeBalanceAmount;}
    double getPenaltyPercentage(){return m_cdPenaltyPercentage;}

    // prepare the cursor like structure (vector in this case)


    vector<Record> queryTransactions(){
        vector<Record> records;
        dataSource.getTransactionsForUser(getUserID());  // similar to cursor like structure
        string eof("EOF");

        string recordLine = dataSource.next();
        while(recordLine.compare(eof) != 0){
            records.push_back(Record(recordLine));
            recordLine = dataSource.next();
        }

        // lambda short cut to sort vector of records
        std::sort(records.begin(), records.end(),
          [] (Record & a, Record & b) {
                return a.getDate().getTimeStamp() < b.getDate().getTimeStamp();
              }
        );

        return records;
    }

    // overload the << operator so that it can understand how to interpret when <<
    // finds object of this class.
    friend ostream& operator<<(ostream& os, const Account& acc){
        os << acc.m_lUserID << ", " << acc.m_strUserName << ", " << acc.m_dOpeningBalance;
        return os;
    }

};

Account::~Account(){}  //still provide default one, this class can't be instantiated alone.

class SavingsAccount: public Account{};  // Leaving it unimplemented for the time being.

// This class inherits Account and reuses the structure.
class CurrentAccount: public Account {
private:
    string m_strReportFileName;
public:
    // ctor mehtod that calls base's version and reuses Accounts member methods
    // to keep the opening balance, userName and records ready
    CurrentAccount(long accNo): Account(accNo)  // call ctor in initialization list.
    {}

    virtual ~CurrentAccount(){}

    void setReportFileName(string fileName){
        m_strReportFileName = fileName;
    }

    // The actual method that iterates through the list of retrieved records, calculates
    // the Daily balance and creates a report.
    void generateStatement(int month){
        if (m_strReportFileName.length() > 0 ){
            ofstream ost;
            ost.open(m_strReportFileName);
            writeReport(ost, month);
            ost.close();
        }else{
            writeReport(cout, month);
        }
    }

    void writeReport(ostream &ost, int month){
        // Filter Records For the Requested Month
        double initialBalance  = getOpeningBalance();
        vector<Record> records = queryTransactions();   // get all the transaction records for this user

        double currentBalance = initialBalance;

		ost.width(111);
        ost.fill('-');
        ost << "\n";
        ost.fill(' ');
        ost    << getUserName()
                << setw(76) << "Opening Balance: " << initialBalance
                << "\n";

        ost.width(111);
        ost.fill('-');
        ost << "\n";
        ost.fill(' ');
        ost << "Date/Time"                 << setw(55)
             << "Description"              << setw(27)
             << "Amount Out(-)/In(+)" << setw(19)
             << "Daily Balance"
             << "\n";
        ost.width(111);
        ost.fill('-');
        ost << "\n";
        ost.fill(' ');
        for(unsigned i =0; i < records.size(); i++){
            if(records[i].date.getMonth() == month){
            currentBalance = currentBalance + records[i].amount;
            // calculate in case if there is a penalty for
            currentBalance = findPenalty(currentBalance);
            ost << records[i].date         << setw(45)
                 << records[i].description  << setw(27)
                 << records[i].amount       << setw(19)
                 << currentBalance          << "\n";

                //ost << records[i];
            }
        }
        // closing balance
        ost.width(111);
        ost.fill('-');
        ost << "\n";
        ost.fill(' ');
        ost    << setw(104) << "Closing Balance: " << currentBalance
                << "\n";
        ost.width(111);
        ost.fill('-');
        ost << "\n\n";

    }
    // This method calculates the penalty and updates the daily balance
    // accordingly when ever the transaction paid out goes below balance
    // limit.
    double findPenalty(double balance){
        if(balance < getSafeBalanceLimit()) {
            double penalty = (balance * getPenaltyPercentage())/100;
            balance=balance-penalty;
        }
        return balance;
    }
};

