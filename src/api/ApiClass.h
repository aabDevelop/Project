#ifndef SRC_API_APICLASS_H_
#define SRC_API_APICLASS_H_

class ApiClass {
public:
	ApiClass();
	ApiClass(int startValue);
	virtual ~ApiClass();

	int method(int vl);


private:
	int value;
};

#endif
