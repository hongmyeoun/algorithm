import java.util.Scanner

fun main(args: Array<String>) {
    val sc: Scanner = Scanner(System.`in`)
    var a = sc.nextInt()
    var b = sc.nextInt()

    val unit = b % 10
    val tens = (b / 10) % 10
    val hudreds = b / 100

    val fisrtResult = a * unit
    val secondResult = a * tens
    val thirdResult = a * hudreds
    val lastResult = fisrtResult + secondResult * 10 + thirdResult * 100

    println(fisrtResult)
    println(secondResult)
    println(thirdResult)
    println(lastResult)
}