from languages.java import JavaTask

# Description
# Implement ConcatStream class that concatenates InputStreams

task = JavaTask()
task.set_solution_class_name("ConcatStream")
task.test_descriptions = ["Checks read() with 1 stream.",
                          "Checks read() with 2 streams.",
                          "Checkss read() with 5 streams. One of them is empty.",
                          "Checks read(byte[]) with 1 stream.",
                          "Checks read(byte[]) with 3 streams. One of them is empty.",
                          "Checks read(byte[]) with 1 stream that lazily generates 100.000.000 bytes.",
                          "Checks read(byte[]) with 5 streams. Each lazily generates 50.000.000.",
                          "Checks read(byte[], int, int) with 1 stream.",
                          "Checks read(byte[], int, int) with 3 streams.",
                          "Checks available() with 5 streams.",
                          "Checks close() with 10 streams."]
