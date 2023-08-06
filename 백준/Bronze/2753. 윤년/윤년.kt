import java.util.Scanner

fun main(args: Array<String>) {
    val sc: Scanner = Scanner(System.`in`)
    val a = sc.nextInt()

    if ((a % 4 == 0 && a % 100 != 0) || a % 400 == 0){
        println("1")
    }else{
        println("0")
    }
}