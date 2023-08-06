import java.util.Scanner

fun main(args: Array<String>) {
    val sc: Scanner = Scanner(System.`in`)
    val a = sc.nextInt()

    when(a){
        in 90..100 -> println("A")
        in 80..89->println("B")
        in 70..79 -> println("C")
        in 60..69->println("D")
        else -> println("F")
    }
}