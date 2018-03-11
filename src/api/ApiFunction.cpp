#include "ApiFunction.h"

#include <cstring>

int apiFunction(int v1, int v2){
	return v1*v2;
}
void apiFunctionMutablePointer(double * value){


	* value = *value * 100;
}


Data apiFunctionGetData(){

	Data dt;

	dt.intValue = 1;
	dt.doubleValue = 3.1415;
	dt.ucharValue = 0xff;

	return dt;
}

Data GLOBAL_DATA;


Data * apiFunctionGetPointerData(){

	GLOBAL_DATA.intValue = 1*2;
	GLOBAL_DATA.doubleValue = 3.1415*2;
	GLOBAL_DATA.ucharValue = 0xAA;

	return &GLOBAL_DATA;
}

void apiFunctionMutablePointerData(Data * data){
	data->intValue = data->intValue * 3;
	data->doubleValue = data->doubleValue *3;
	data->ucharValue = data->ucharValue * 3;
}


BigData apiFunctionGetBigData(){
	BigData bd;

	bd.iv = 1;
	bd.v1 = 2;
	bd.v2 = 3;
	bd.v3 = 4;
	bd.v4 = 5;

	std::memset(bd.st,0,12);
	std::memmove(bd.st,"hello world",12);

	return bd;
}
