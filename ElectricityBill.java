import java.util.*;
public Class ElctricityBill{
Public static void main(String[] args){
int units ,charge,amount;
Scanner scanner = new Scanner(System.int);
System.out.println("enter a number:");
int meterno = Scanner.nextInt();
System.out.println("enter previous reading");
int previous = Scanner.nextInt();
System.out.println("enter present reading");
int present = Scanner.nextInt();
if(previous<present){
units=present-previous;
System.out.println("units is:"+units);
if(units > 0 && units <= 100){
charge = 2;
}
else if(units > 101 && units <= 200){
charge=4;
}
else{
charge=5;
}
System.out.println("charge is:"+charge);
amount=units*charge;
System.out.println("amount is:"+amount);
}
else{
System.out.println("please enter valid reading");
}
}
}