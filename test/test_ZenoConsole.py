from unittest import TestCase, mock, main


from zeno.zenoconsole import ZenoConsole

class TestZenoConsole(TestCase):
    def test_zeno_console(self):
        captured_logs = []
        buffermock = mock.Mock()
        # buffer.write = lambda message: captured_logs.append(message)

        MESSAGE = "I'm thinking of something"
        def mockinput(prompt):
            print(f"Got called with prompt: {prompt}")
            return MESSAGE

        console = ZenoConsole(buffermock, input_function=mockinput)
        console.start(loopOnce=True)
        callslist = buffermock.write.call_args_list

        # self.assertRegex(callslist[0], r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$')
        self.assertEqual(callslist[2], mock.call("\n\n"))
        self.assertEqual(callslist[3], mock.call(MESSAGE))
        self.assertEqual(callslist[4], mock.call("\n\n"))
        self.assertEqual(callslist[5], mock.call("-" * 80))
        # self.assertEqual(callslist[3], r'-+')

if __name__ == '__main__':
    main()
