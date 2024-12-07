#include <iostream>
using namespace std;

// This program has been created to calculate shapes.
int start_panel() {
    int shape;
    // Assumed that the user will enter the number.
    cout << "What shape would you like to examine? (type number)" << endl;
    cout << "1. Circle" << endl;
    cout << "2. Square" << endl;
    cout << "3. Triangle" << endl;
    cin >> shape;

    return shape;
}

void circle(float radius){
    float pi = 3.14159;
    float area = pi*(radius*radius);
    float perimeter = 2*pi*radius;
    cout << "Area of the circle: " << area << endl;
    cout << "Perimeter of the circle: " << perimeter << endl;
}

void square(float length, float height){
    float area = length*height;
    float perimeter = (2*length)+(2*height);
    cout << "Area of the square: " << area << endl;
    cout << "Perimeter of the square: " << perimeter << endl;
}

void triangle(float length, float height){
    float area = (length*height)/2;
    float perimeter = (3*length); // assume all lenghts the same
    cout << "Area of the triangle: " << area << endl;
    cout << "Perimeter of the triangle: " << perimeter << endl;
}



int main() {
    cout << "|=================================|" << endl;
    cout << "|======= Program Started =========|" << endl;
    cout << "|=================================|" << endl;
    cout << endl;

    int shape;
    float radius;
    float length;
    float height;
    bool run = true;

    shape = start_panel();
    while (run == true) {
        if (shape == 1) {
            // ask user for radius
            // Call Circle (area and perimeter)
            cout << "What is the radius of the circle?" << endl;
            cin >> radius;
            circle(radius);
            cout << endl;
        } else if (shape == 2) {
            cout << "What is the length of the square?" << endl;
            cin >> length;
            cout << "What is the height of the square?" << endl;
            cin >> height;
            square(length,height);
            cout << endl;
        } else if (shape == 3) {
            cout << "What is the length of the triangle?" << endl;
            cin >> length;
            cout << "What is the height of the triangle?" << endl;
            cin >> height;
            triangle(length,height);
            cout << endl;
        } else {
            cout << "Error: The shape you entered was not regognised." << endl;
            // Create error handling function. then call here.
            break;
        }
        cout << "Would you like another calculation?" << endl;
        char response;
        cin >> response;
        if (response == 'y') {
            shape = start_panel();
            continue;
        } else {
            run = false;
        }

    }
    cout << endl;
    cout << "|=================================|" << endl;
    cout << "|======== Program Ended ==========|" << endl;
    cout << "|=================================|" << endl;
    return 0;
}
