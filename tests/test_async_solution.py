import asyncio
import importlib.machinery
import importlib.util
import io
from contextlib import redirect_stdout
from pathlib import Path
import unittest


def load_sample():
    sample_path = Path(__file__).parents[1] / "test_python"
    loader = importlib.machinery.SourceFileLoader("async_sample", str(sample_path))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


class AsyncSolutionTests(unittest.IsolatedAsyncioTestCase):
    async def test_greeting_returns_named_message(self):
        sample = load_sample()

        message = await sample.greeting("Ada", 0)

        self.assertEqual(message, "hello, Ada")

    async def test_solution_prints_each_greeting(self):
        sample = load_sample()
        output = io.StringIO()

        with redirect_stdout(output):
            await sample.solution()

        self.assertEqual(output.getvalue().splitlines(), ["hello, Alice", "hello, Bob"])


if __name__ == "__main__":
    unittest.main()