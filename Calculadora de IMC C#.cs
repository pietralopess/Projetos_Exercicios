using System;

class Program
{
    static void Main()
    {
        Console.Write("Digite seu peso (kg): ");
        double peso = Convert.ToDouble(Console.ReadLine());
        
        Console.Write("Digite sua altura (m): ");
        double altura = Convert.ToDouble(Console.ReadLine());
        
        double imc = peso / (altura * altura);
        Console.WriteLine($"Seu IMC é: {imc:F2}");
        
        if (imc < 18.5)
        {
            Console.WriteLine("Classificação: Abaixo do peso");
        }
        else if (imc >= 18.5 && imc < 24.9)
        {
            Console.WriteLine("Classificação: Peso normal");
        }
        else if (imc >= 25 && imc < 29.9)
        {
            Console.WriteLine("Classificação: Sobrepeso");
        }
        else if (imc >= 30 && imc < 34.9)
        {
            Console.WriteLine("Classificação: Obesidade grau 1");
        }
        else if (imc >= 35 && imc < 39.9)
        {
            Console.WriteLine("Classificação: Obesidade grau 2");
        }
        else
        {
            Console.WriteLine("Classificação: Obesidade grau 3 (mórbida)");
        }
    }
}
