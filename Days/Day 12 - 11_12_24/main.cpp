//
//
//
//

/*
ofstream	Creates and writes to files
ifstream	Reads from files
fstream		A combination of ofstream and ifstream: creates, reads, and writes to files


 */

#include <iostream>
#include <fstream>
#include <string>


using namespace std;

int main() {
    cout << "===== Program Started =====" << endl << endl;
	/*string file_content;

	//double TotalValue = 0, TotalConsumption = 0;
	ifstream TextFile("equipment.txt");


	// Use a while loop together with the getline() function to read the file line by line
	while (getline(TextFile, file_content)) {
		// Output the text from the file
		cout << file_content;
	}

	TextFile.close();*/

	// Create a text string, which is used to output the text file
	string myText;

	// Read from the text file
	ifstream MyReadFile("filename.txt");

	// Use a while loop together with the getline() function to read the file line by line
	while (getline (MyReadFile, myText)) {
		// Output the text from the file
		cout << myText;
	}

	// Close the file
	MyReadFile.close();
    return 0;
}

