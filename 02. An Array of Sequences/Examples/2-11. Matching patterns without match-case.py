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
    if isinstance(exp, Symbol):  # variable reference
        return env[exp]
    # ... lines omitted.
    elif exp[0] == 'quote':  # (quote x)
        _, x = exp
        return x
    elif exp[0] == 'if':  # (if test consequence alternative)
        _, test, consequence, alternative = exp
        if evaluate(test, env):
            return evaluate(consequence, env)
        else:
            return evaluate(alternative, env)
    elif exp[0] == 'lambda':  # (lambda (parms…) body…)
        _, parms, *body = exp
        return Procedure(parms, body, env)
    elif exp[0] == 'define':
        _, name, value_exp = exp  # (define name value_exp)
        env[name] = evaluate(value_exp, env)
    # ... more lines omitted.
