import java.util.Scanner

fun main(args: Array<String>) {
    val sc: Scanner = Scanner(System.`in`)
    var a = sc.nextInt()
    var b = sc.nextInt()
    var c = sc.nextInt()

    var firstResult = (a + b) % c
    var secondResult = ((a % c) + (b % c)) % c
    var thirdResult = (a * b) % c
    var fourthResult = ((a % c) * (b % c)) % c

    println(firstResult)
    println(secondResult)
    println(thirdResult)
    println(fourthResult)
}