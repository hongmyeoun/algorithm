import java.util.Scanner

fun main(args: Array<String>) {
    val sc: Scanner = Scanner(System.`in`)
    var hour = sc.nextInt()
    var minute = sc.nextInt()
    val runTime = sc.nextInt()

    //hour minute 출력
    //runHour = runTime / 60
    //runMinute = runTime % 60
    //hour = hour + runHour
    //minute = minute + runMinute
    //if minute > 59
    //hour += 1
    //minute = minute + (minute % 60)
    //if hour > 24
    //hour = 0

    val runHour = runTime / 60
    val runMinute = runTime % 60
    hour += runHour
    minute += runMinute
    if (minute >= 60) {
        hour += 1
        minute %= 60
    }
    if (hour >= 24) {
        hour %= 24
    }
    println("$hour $minute")

}