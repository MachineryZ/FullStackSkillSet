#include <iostream>
using namespace std;

double power(int x, int n)
{
    int ret = 1;
    while(n > 0)
    {
        ret *= x;
        n--;
    }
    return ret;
}

int main(int argc, char const *argv[])
{
    int x;
    int n;
    cin >> x >> n;
    cout << power(x, n) << endl;

    return 0;
}