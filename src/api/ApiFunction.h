#ifndef SRC_API_APIFUNCTION_H_
#define SRC_API_APIFUNCTION_H_


#ifdef __cplusplus
extern "C" {
#endif

int apiFunction(int v1, int v2);

void apiFunctionMutablePointer(double * value);

struct Data{
	int intValue;
	double doubleValue;
	unsigned char ucharValue;
};


struct BigData{
	int iv;
	int v1:4;
	int v2:4;
	int v3:8;
	int v4:16;

	char st[12];

};


Data apiFunctionGetData();

Data * apiFunctionGetPointerData();

void apiFunctionMutablePointerData(Data * data);

BigData apiFunctionGetBigData();


#ifdef __cplusplus
}
#endif

#endif
