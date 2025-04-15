import python

/**
 * @name SQL Injection Detection
 * @description Finds potential SQL injection vulnerabilities in Python code.
 * @kind problem
 * @problem.severity error
 * @id py/sql-injection
 */

from CallExpr call, Expr taintedInput
where
  // Identify calls to execute() or executemany() methods of database cursors
  call.getTarget().getName() = "execute" or
  call.getTarget().getName() = "executemany" and
  call.getQualifier().getType().getName().matches(".*cursor.*") and
  // Check if the argument to the method is tainted by user input
  taintedInput = call.getArgument(0) and
  taintedInput.isTainted()
select call, "Potential SQL injection vulnerability."