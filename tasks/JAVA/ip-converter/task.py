from languages.java import JavaTask

# Description
# Implement converter of IPv4 addresses. ipToDec, ipToBin, ipToHex.

task = JavaTask()
task.set_solution_class_name("IpConverter")
task.test_descriptions = ["Decimal ip. Check toDec(), toHex(), toBin().",
                          "Hex ip. Check toDec(), toHex(), toBin().",
                          "Binary ip. Check toDec(), toHex(), toBin()."]
