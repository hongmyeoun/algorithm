import java.util.Scanner

fun main(args: Array<String>){
    val sc: Scanner = Scanner(System.`in`)
    val n = sc.nextInt()
    var result = 0
    for (i in 1..n){
        result += i
    }
    println(result)
}