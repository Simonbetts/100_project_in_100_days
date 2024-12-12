// 100 Projects in 100 Days
// INPUT: N/A
// OUTPUT: N/A
// By Simon A. Betts 12/12/2024

/*
 Day 13 - Stock Management System

The Stock Management System in C++ is a program designed to help businesses manage their stock levels.
It tracks the current inventory of products and allows users to add, delete and modify items in the inventory.
Technologies used in this project include C++ and SQLite. SQLite is used to store and manage data.
C++ is used for the program’s backend, allowing for the stock management system to be easily modified and extended.
The Stock Management System is a powerful tool that can help store owners and managers keep track of their stock,
allowing them to make the most of their resources.

Possible Solutions: C++ programming language, Object-oriented Programming (OOP),
Relational Database Management System(RDBMS), Structured Query Language(SQL) and Multi-threading.
source: https://www.geeksforgeeks.org/top-50-cpp-project-ideas-for-beginners-advanced/#beginner-level-c-projects-ideas
*/

#include <iostream>
#include <fstream>
#include <string>
using namespace std;


void start();
void end();

int main() {

    start();
    string file_name = "stock_log.txt";
    string doctext;
    ifstream file;
    file.open(file_name);


    if(file) {
        cout << "Stock Log File Exists" << endl << endl;
    } else {
        cout << "Stock Log File does not exists" << endl; // printing the error message
        ofstream file(file_name); // creating a file
        cout << "Stock Log File created" << endl << endl;
        file.close();
        file.open(file_name);
    }

    bool running = true;
    int i = 0;

    while (running == true) {

        // Output current data in stock log
        cout << "|== The Stock Log Currently Contains: ==|" << endl;
        while (getline (file, doctext)) {
            cout << doctext << endl;  // Output the text from the file
        } cout << endl;

        // Request to add
        string answer;
        cout << "Would you like to add to the stock list? (y = yes, n = no)" << endl;
        cin >> answer;
        cout << endl;

        if (answer == "y") {
            string item_name;
            int item_qty;
            double item_cost;


            cout << "What is the name of the item?" << endl;
            cin >> item_name;
            cout << "How many of the item?" << endl;
            cin >> item_qty;
            cout << "How much is the item?" << endl;
            cin >> item_cost;

            cout << "The item: " << item_name << "Quantity: " << item_qty << "Cost: " << item_cost << endl;
            cout << "added to list" << endl << endl;


            fstream MyFile("stock_log.txt");   // Create and open a text file

            MyFile << item_name << " " << item_qty << " " << item_cost; // Write to the file
            MyFile.close(); // Close the file

        } else if (answer == "n") {
            cout << "No addtional items assed"<< endl;
        } else {
            cout << "Answer not recognised"<< endl;
        }

        // if statmtent
        while (i < 5) {
            cout << i << "\n";
            i++;
        }
        cout << endl;
        running = false;
    }

    file.close();
    end();
    return 0;
}

void start() {
    cout << "|===========================|" << endl;
    cout << "|===== PROGRAM STARTED =====|" << endl;
    cout << "|===========================|" << endl << endl;
}

void end() {
    cout << "|===========================|" << endl;
    cout << "|====== PROGRAM ENDED ======|" << endl;
    cout << "|===========================|" << endl << endl;
}

/* Useful Links
https://www.scaler.com/topics/cpp-check-if-the-file-exists/

*/