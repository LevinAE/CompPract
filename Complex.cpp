#include <iostream>
#include <math.h>
#include <complex>
#include <iomanip>
using namespace std;

int main() {
    int k;
    double real, imag, z_real, z_imag, n_rt;

    complex< double > z1( 1.0, 1.0 );
    complex< double > z2( 4.0, 1.0 );
    complex< double > z3( 1.0, -2.0 );

    cout << "Сложение комплексных чисел: z1 + z2=" <<  z1 + z2 << endl; // Сложение комплексных чисел
    cout << "Разность комплексных чисел: z1 - z2=" << z1 - z2 << endl; // Разность комплексных чисел
    cout << "Умножение комплексных чисел: z1 * z2=" << z1 * z2 << endl; // Умножение комплексных чисел
    cout << "Деление комплексных чисел: z1 / z2=" << z1 / z2 << endl; // Деление комплексных чисел
    cout << "Возведение в степень комплексного числа: z^4=" << pow( z3, 4 ) << endl; // Возведение в степень комплексного числа
    double rho = abs( z3 ); // Модуль комплексного числа
    double phi = arg( z3 ); // Аргумент комплексного числа
// Извлечение корня n степени из комплексного числа
    cout << "Input complex number ";
    cin >> real >> imag; // Ввод действительной и мнимой части через пробел
    complex<double> zp(real, imag);
    cout << fixed << setprecision(16) << zp << endl;
    cout << "Input number n ";
    cin >> n_rt;
    cout << "\n";
    rho = abs( zp );
    phi = arg( zp );
    cout << "rho=" << rho << ", phi=" << phi << endl;
    for(k=0; k<n_rt; k++)
    {
        z_real = pow( rho, float (1/n_rt)) * cos((phi + 2 * M_PI * k) / n_rt);
        z_imag = pow( rho, float (1/n_rt)) * sin((phi + 2 * M_PI * k) / n_rt);
        complex<double> z_n(z_real, z_imag);
        cout << "k=" <<k<<  ", z_k=" << z_n << "\n";
    }
    return 0;
}