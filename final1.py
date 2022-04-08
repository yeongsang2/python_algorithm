#include <iostream>
#include <string>
#include <valarray>
#include <vector>
#include <fstream>
using namespace std;

// 세게의 파일을 받아 ->흑백이미지 곂치게하기

int main() {
	string file1, file2, file3, ofilename;
	cout << "Input three files: ";
	cin >> file1 >> file2 >> file3;
	cout << "out filename: ";
	cin >> ofilename;

	ifstream fin1(file1, ios::in, ios::binary);
	ifstream fin2(file2, ios::in, ios::binary);
	ifstream fin3(file3, ios::in, ios::binary);

	if (!fin1) {
		cout << "파일열기 실패";
	}
	if (!fin2) {
		cout << "파일열기 실패";
	}
	if (!fin3) {
		cout << "파일열기 실패";
	}
	string magic1, magic2, magic3;
	int w1, h1, w2, h2, w3, h3;
	fin1 >> magic1 >> w1 >> h1;
	fin2 >> magic2 >> w2 >> h2;
	fin3 >> magic3 >> w3 >> h3;

	fin1.seekg(-w1 * h1 | ios::end); //end로부터 -w*h
	fin2.seekg(-w2 * h2 | ios::end);
	fin3.seekg(-w3 * h3 | ios::end);

	vector<unsigned char> data1;
	vector<unsigned char> data2;
	vector<unsigned char> data3;

	while (!fin1.eof())
	{
		data1.push_back(fin1.get());
	}
	while (!fin2.eof())
	{
		data2.push_back(fin2.get());
	}
	while (!fin3.eof()) {
		data3.push_back(fin3.get());
	}
	int size = data1.size();
	valarray<unsigned char> pixel1(size);
	valarray<unsigned char> pixel2(size);
	valarray<unsigned char> pixel3(size);

	valarray<unsigned char> film(size);

	for (int i = 0; i < size; i++) {
		pixel1[i] = data1[i];
		pixel2[i] = data2[i];
		pixel3[i] = data3[i];
	}

	film = pixel1 + pixel2 + pixel3;

	ofstream fout(ofilename, ios::out | ios::binary);
	if (!fout) {
		cout << "파일 열기 실패띠";
	}
	fout.seekp(0, ios::end);
	fout << magic1 << " " << w1 << " " << h1 << " 255\n";
	for (int i = 0; i < size; i++) {
		fout << film[i];
	}
	fin1.close();
	fin2.close();
	fin3.close();
	fout.close();

	return 0;
	
}