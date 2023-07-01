from typing import Any

Environment = dict
Expression = list
Symbol = object


class Procedure:
    def __init__(self, parms, body, env):
        self.parms = parms
        self.body = body
        self.env = env


def evaluate(exp: Expression, env: Environment) -> Any:
    """Evaluate an expression in an environment."""
    match exp:
        # ... lines omitted.
        # Match if subject is a two-item sequence starting with 'quote'.
        case ['quote', x]:
            return x
        # Match if subject is a four-item sequence starting with 'if'.
        case ['if', test, consequence, alternative]:
            if evaluate(test, env):
                return evaluate(consequence, env)
            else:
                return evaluate(alternative, env)
        # Match if subject is a sequence of three or more items starting with
        # 'lambda'. The guard ensures that body is not empty.
        case ['lambda', [*parms], *body] if body:
            return Procedure(parms, body, env)
        # Match if subject is a three-item sequence starting with 'define',
        # followed by an instance of Symbol.
        case ['define', Symbol() as name, value_exp]:
            env[name] = evaluate(value_exp, env)
        # Shortcut syntax for function definition:
        # (define (name parms…) body1 body2…)
        case ['define', [Symbol() as name, *parms], *body] if body:
            env[name] = Procedure(parms, body, env)
        # ... more lines omitted.
        # It is good practice to have a catch-all case. In this example, if exp
        # doesn't match any of the patterns, the expression is malformed, and I
        # raise SyntaxError.
        case _:
            raise SyntaxError(lispstr(exp))


def lispstr(_):
    pass
