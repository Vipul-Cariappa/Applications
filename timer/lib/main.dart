import 'package:flutter_beep/flutter_beep.dart';
import 'package:flutter/material.dart';
import 'dart:async';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Timer Application'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  Timer? countdownTimer;
  Duration myDuration = const Duration(seconds: 30);

  List<int> durationSecondsList = [];

  int countUp = 0;

  final hhController = TextEditingController();
  final mmController = TextEditingController();
  final ssController = TextEditingController();

  String listTimerText = "";

  void setCountDown(Timer timer) {
    const reduceSecondsBy = 1;
    setState(() {
      final seconds = myDuration.inSeconds - reduceSecondsBy;
      countUp++;

      listTimerText = "";

      for (int i = 0; i < durationSecondsList.length; i++) {
        int d = durationSecondsList[i];
        listTimerText += "\n$d";
        durationSecondsList[i] = durationSecondsList[i] - 1;

        if (durationSecondsList.elementAt(i) < 0) {
          durationSecondsList.removeAt(i);
          FlutterBeep.beep();
        }
      }

      if (seconds < 0) {
        timer.cancel();
        FlutterBeep.beep(false);
      } else {
        myDuration = Duration(seconds: seconds);
      }
    });
  }

  void addTimer() {
    int? hour = int.parse(hhController.text != "" ? hhController.text : "0");
    int? min = int.parse(mmController.text != "" ? mmController.text : "0");
    int? second = int.parse(ssController.text != "" ? ssController.text : "0");

    if (!(0 <= hour) && !(hour <= 24)) {
      hour = 0;
    }
    if (!(0 <= min) && !(min <= 60)) {
      min = 0;
    }
    if (!(0 <= second) && !(second <= 60)) {
      second = 0;
    }

    countUp = 0;

    setState(() {
      int duration = second! + min! * 60 + hour! * 60 * 60;

      if (duration != 0) {
        durationSecondsList.add(duration);

        listTimerText += "\n$duration";
      } else {
        durationSecondsList.add(30);

        listTimerText += "\n30";
      }

      int largest = 0;
      for (final i in durationSecondsList) {
        if (largest < i) {
          largest = i;
        }
      }
      myDuration = Duration(seconds: largest);
    });
  }

  void startTimer() {
    countdownTimer =
        Timer.periodic(const Duration(seconds: 1), (_) => setCountDown(_));
  }

  void stopTimer() {
    setState(() => countdownTimer!.cancel());
  }

  void resetTimer() {
    stopTimer();

    setState(() {
      listTimerText = "";
      hhController.text = "";
      mmController.text = "";
      ssController.text = "";

      durationSecondsList.clear();

      myDuration = const Duration(seconds: 30);
    });
  }

  @override
  void dispose() {
    hhController.dispose();
    mmController.dispose();
    ssController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    String hhValue = myDuration.inHours.remainder(24).toString();
    String mmValue = myDuration.inMinutes.remainder(60).toString();
    String ssValue = myDuration.inSeconds.remainder(60).toString();

    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: <Widget>[
            Text(
              "$hhValue:$mmValue:$ssValue",
              style: const TextStyle(fontSize: 38),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                SizedBox(
                  width: 80,
                  child: TextField(
                    keyboardType: TextInputType.number,
                    controller: hhController,
                    style: const TextStyle(fontSize: 28),
                    decoration: const InputDecoration(
                      border: OutlineInputBorder(),
                      hintText: 'HH',
                    ),
                  ),
                ),
                SizedBox(
                  width: 80,
                  child: TextField(
                    keyboardType: TextInputType.number,
                    controller: mmController,
                    style: const TextStyle(fontSize: 28),
                    decoration: const InputDecoration(
                      border: OutlineInputBorder(
                        gapPadding: 1,
                      ),
                      hintText: 'MM',
                    ),
                  ),
                ),
                SizedBox(
                  width: 80,
                  child: TextField(
                    keyboardType: TextInputType.number,
                    controller: ssController,
                    style: const TextStyle(fontSize: 28),
                    decoration: const InputDecoration(
                      border: OutlineInputBorder(),
                      hintText: 'SS',
                    ),
                  ),
                ),
              ],
            ),
            ElevatedButton(
              onPressed: startTimer,
              child: const Text(
                'Start',
                style: TextStyle(fontSize: 28),
              ),
            ),
            ElevatedButton(
              onPressed: () {
                if (countdownTimer == null || countdownTimer!.isActive) {
                  stopTimer();
                }
              },
              child: const Text(
                'Stop',
                style: TextStyle(
                  fontSize: 30,
                ),
              ),
            ),
            ElevatedButton(
              onPressed: () {
                resetTimer();
              },
              child: const Text(
                'Reset',
                style: TextStyle(
                  fontSize: 30,
                ),
              ),
            ),
            ElevatedButton(
              onPressed: addTimer,
              child: const Text(
                'Add',
                style: TextStyle(fontSize: 28),
              ),
            ),
            Text(
              listTimerText,
              style: const TextStyle(fontSize: 38),
            ),
          ],
        ),
      ),
    );
  }
}
