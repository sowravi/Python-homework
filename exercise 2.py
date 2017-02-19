from __future__ import print_function, division
import cmd


class Mycmd(cmd.Cmd):
    prompt = 'mycmd >>> '
    intro = 'My Command prompt'

    def do_deploy(self, line):
        print("Deploy")

    def do_kill(self, line):
        print("Kill")

    def do_benchmark(self, line):
        print("Benchmark")

    def do_report(self, line):
        print("Report")

    def do_EOF(self, line):
        print('bye, bye')
        return True


if __name__ == '__main__':
    Mycmd().cmdloop()
