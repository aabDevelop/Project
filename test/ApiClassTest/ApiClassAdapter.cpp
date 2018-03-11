#include "ApiClass.h"

#ifdef __cplusplus
extern "C" {
#endif

ApiClass * pEmptyApiClass = 0;
ApiClass * pApiClass = 0;

void createEmptyApiClass(){
	if(pEmptyApiClass != 0){
		delete pEmptyApiClass;
	}
	pEmptyApiClass = new ApiClass;
}
void deleteEmptyApiClass(){
	if(pEmptyApiClass != 0){
		delete pEmptyApiClass;
		pEmptyApiClass=0;
	}
}

void createApiClass(int value){
	if(pApiClass != 0){
		delete pApiClass;
	}
	pApiClass = new ApiClass(value);
}
void deleteApiClass(){
	if(pApiClass != 0){
		delete pApiClass;
		pApiClass=0;
	}
}

int callEmptyApiClassMethod(int vl){
	return pEmptyApiClass->method(vl);
}

int callApiClassMethod(int vl){
	return pApiClass->method(vl);
}





#ifdef __cplusplus
}
#endif
