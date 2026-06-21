#!/usr/bin/env python3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "html" / "_sources"


SOURCE_TEXTS = {
    "index.rst.txt": r"""
证明的技艺
==========

本书讨论如何书写细致而严谨的数学证明。本书配有以计算机形式化语言
`Lean <https://leanprover.github.io/about/>`_ 写成的代码。请前往配套的 GitHub 仓库
https://github.com/hrmacbeth/math2001，将这些代码下载到自己的计算机，或在 Gitpod 云端打开。

本书面向大学低年级学生，并为 Fordham University 的 Math 2001 课程而写。若有意见或修正，欢迎联系作者
`Heather Macbeth <https://faculty.fordham.edu/hmacbeth1/>`_。

.. toctree::
   :maxdepth: 2

   00_Introduction

.. toctree::
   :numbered:
   :maxdepth: 2

   01_Proofs_by_Calculation
   02_Proofs_with_Structure
   03_Parity_and_Divisibility
   04_Proofs_with_Structure_II
   05_Logic
   06_Induction
   07_Number_Theory
   08_Functions
   09_Sets
   10_Relations

**附录**

.. toctree::
   Index_of_Tactics
   Mainstream_Lean
""",
    "Homework.rst.txt": r"""
.. _homework:

作业
====

.. include:: Homework/hw0.inc
""",
    "01_Proofs_by_Calculation.rst.txt": r"""
.. raw:: latex

    \mainmatter

.. _proofs_by_calculation:

计算式证明
==========

本书从熟悉的数的世界开始：:math:`\mathbb{N}`，即自然数（本书中包含 0）；
:math:`\mathbb{Z}`，即整数；:math:`\mathbb{Q}`，即有理数；以及
:math:`\mathbb{R}`，即实数。我们要解决一些很接近高中代数的问题：从已有等式或不等式推出新的等式或不等式。不过，我们使用的技巧通常并不在高中代数中讲授：构造一条单一的表达式链，把左边与右边连接起来。

.. include:: ch01_Proofs_by_Calculation/01_Proving_Equalities.inc
.. include:: ch01_Proofs_by_Calculation/02_Proving_Equalities_in_Lean.inc
.. include:: ch01_Proofs_by_Calculation/03_Tips_and_Tricks.inc
.. include:: ch01_Proofs_by_Calculation/04_Proving_Inequalities.inc
.. include:: ch01_Proofs_by_Calculation/05_A_Shortcut.inc
""",
    "02_Proofs_with_Structure.rst.txt": r"""
.. _proofs_with_structure:

有结构的证明
============

从某种角度看，:numref:`第 %s 章 <proofs_by_calculation>`中的计算式证明全都是一步证明。在本章中，我们逐渐引入多步证明的组成部分。这些组成部分包括：建立之后会再次引用的“中间”事实；调用由你自己或他人先前证明过的具名引理；以及拆解由较简单陈述通过逻辑符号 :math:`\lor`、:math:`\land` 和 :math:`\exists` 组合而成的复杂数学陈述。

本章还介绍 Lean 语言的关键交互功能：实时更新的 *infoview*，它会跟踪你当前的假设和目标。

本章的工作会在中间插入一章之后，于 :numref:`第 %s 章 <proofs_with_structure_ii>`继续。

.. include:: ch02_Proofs_with_Structure/01_Intermediate_Steps.inc
.. include:: ch02_Proofs_with_Structure/02_Invoking_Lemmas.inc
.. include:: ch02_Proofs_with_Structure/03_Or.inc
.. include:: ch02_Proofs_with_Structure/04_And.inc
.. include:: ch02_Proofs_with_Structure/05_Exists.inc
""",
    "03_Parity_and_Divisibility.rst.txt": r"""
.. _parity_and_divisibility:

奇偶性与整除性
==============

本章的问题涉及自然数和整数的一些初等性质：*奇偶性*（一个数是*偶数*还是*奇数*）、*整除性*，以及*模* :math:`n` *同余*。

本章没有像 :math:`\lor` 或 :math:`\exists` 这样的新逻辑符号，也不会对我们的推理工具箱作重大补充（例如使用中间步骤或引理）。因此，本章在 :numref:`第 %s 章 <proofs_with_structure>`和 :numref:`第 %s 章 <proofs_with_structure_ii>`的艰苦工作之间起到喘息作用，让你有机会巩固已经学到的内容。

.. include:: ch03_Parity_and_Divisibility/01_Parity.inc
.. include:: ch03_Parity_and_Divisibility/02_Divisibility.inc
.. include:: ch03_Parity_and_Divisibility/03_Modular_Arithmetic_Theory.inc
.. include:: ch03_Parity_and_Divisibility/04_Modular_Arithmetic_Calculations.inc
.. include:: ch03_Parity_and_Divisibility/05_Bezout.inc
""",
    "04_Proofs_with_Structure_II.rst.txt": r"""
.. _proofs_with_structure_ii:

有结构的证明（二）
==================

在 :numref:`第 %s 章 <proofs_with_structure>`中，我们学习了逻辑符号 :math:`\lor`、:math:`\land` 和 :math:`\exists`。这些符号允许我们由较简单的陈述构造复杂的数学陈述。对于每个这样的符号，我们都学习了它的“语法”：当它出现在假设中时如何使用，以及当它出现在目标中时如何使用。这套语法称为 `自然演绎 <https://en.wikipedia.org/wiki/Natural_deduction>`_。

本章完成 :numref:`第 %s 章 <proofs_with_structure>`中开始的工作。我们学习剩余逻辑符号 :math:`\forall`、:math:`\to` 和 :math:`\lnot` 的语法。我们还学习另外两个逻辑符号 :math:`\leftrightarrow` 和 :math:`\exists!` 的语法；它们不那么基本，因为可以用其他符号来定义。

.. include:: ch04_Proofs_with_Structure_II/01_Forall_Implies.inc
.. include:: ch04_Proofs_with_Structure_II/02_Iff.inc
.. include:: ch04_Proofs_with_Structure_II/03_Exists_Unique.inc
.. include:: ch04_Proofs_with_Structure_II/04_Contradictory_Hypotheses.inc
.. include:: ch04_Proofs_with_Structure_II/05_Proof_by_Contradiction.inc
""",
    "05_Logic.rst.txt": r"""
.. _logic:

逻辑
====

在 :numref:`第 %s 章 <proofs_with_structure>`和 :numref:`第 %s 章 <proofs_with_structure_ii>`中，我们学习了各种逻辑符号的“语法”，例如 :math:`\land`、:math:`\forall` 和 :math:`\to`。在那些章节中，逻辑推理发生在相当具体的数学情境中：关于自然数、有理数等对象的等式和不等式问题。

本章采取更抽象的观点，研究逻辑推理过程本身。中心概念是*逻辑等价*：对一个陈述的逻辑结构所作的、总是有效的变换；之所以总是有效，是因为变换前后的陈述可以仅靠抽象逻辑推理相互推出，而不依赖当前数学情境中的特殊内容。

最重要的逻辑等价是本章最后一节 :numref:`第 %s 节 <negation_normalize>` 中讨论的那些。它们会把否定符号（:math:`\lnot`）移动到逻辑陈述中更深的位置。合在一起，这些变换给了我们一种推迟并尽量减少与 :math:`\lnot` 打交道的方法；它是最别扭的逻辑符号。

.. include:: ch05_Logic/01_Logical_Equivalence.inc
.. include:: ch05_Logic/02_Excluded_Middle.inc
.. include:: ch05_Logic/03_Negation_Algorithm.inc
""",
    "06_Induction.rst.txt": r"""
.. _induction:

归纳法
======

本章介绍*归纳法*，这是一种适用于自然数以及整数、自然数对等其他离散类型的证明方法。我们还介绍*递归*，即定义序列（更一般地说，定义从离散类型出发的函数）的方法；对于递归定义的对象，归纳法是证明相关结论的典范方法。

在 :numref:`第 %s 节 <induction_intro>` 到 :numref:`第 %s 节 <two_step_induction>` 中，我们只使用最传统的归纳形式：通过把自然数处的结论与前一个自然数处的结论联系起来，来证明关于自然数的结果，并讨论这种归纳形式的一些小变体。在 :numref:`第 %s 节 <strong_induction>` 到 :numref:`第 %s 节 <euclidean_algorithm>` 中，我们介绍*强归纳法*，以及更一般的*良基归纳法*。这些归纳原理更加灵活。

.. include:: ch06_Induction/01_Induction.inc
.. include:: ch06_Induction/02_Recurrence_Relations.inc
.. include:: ch06_Induction/03_Two_Step_Induction.inc
.. include:: ch06_Induction/04_Strong_Induction.inc
.. include:: ch06_Induction/05_Pascal.inc
.. include:: ch06_Induction/06_Division_Algorithm.inc
.. include:: ch06_Induction/07_Euclidean_Algorithm.inc
""",
    "07_Number_Theory.rst.txt": r"""
.. _number_theory:

数论
====

本章在风格上不同于本书其他章节。这里的事实都是著名定理，它们的证明需要一次性的巧妙想法。这些特定想法不会再次出现在作业或考试中。不妨把本章看作一个总结性章节：我们探索借助本书到目前为止已经发展出的推理工具和理论，能够触及哪些数学陈述。

.. include:: ch07_Number_Theory/01_Infinitely_Many_Primes.inc
.. include:: ch07_Number_Theory/02_Euclid_Lemma.inc
.. include:: ch07_Number_Theory/03_Sqrt_Two.inc
""",
    "08_Functions.rst.txt": r"""
.. _functions:

函数
====

到目前为止，本书研究的是数的性质（一个数是否为奇数、正数、素数；一个数是否被另一个数整除）以及数上的运算（加法、最大公因数）。

本章我们提升一个抽象层次，研究函数的性质以及函数上的运算。这些新性质包括：一个函数是否为*单射*、*满射*、*双射*；一个函数是否是另一个函数的*逆*；以及*复合*这一运算。

我们还把视野扩展到早期章节所处的数值类型（:math:`\mathbb{N}`、:math:`\mathbb{Z}`、:math:`\mathbb{Q}`、:math:`\mathbb{R}`）之外。现在我们开始处理范围更广的类型，包括函数类型、有限归纳类型和积类型。

.. include:: ch08_Functions/01_Injective_Surjective.inc
.. include:: ch08_Functions/02_Bijective.inc
.. include:: ch08_Functions/03_Composition.inc
.. include:: ch08_Functions/04_Product_Types.inc
""",
    "09_Sets.rst.txt": r"""
.. _sets:

集合
====

本章介绍*集合*语言。它是一种便利的方式，用来讨论某个类型中满足某种性质的对象。这个语言包括集合中的*属于*关系、一个集合是另一个集合的*子集*这一性质，以及一整套集合运算，例如*交*、*并*和*补*；每一种运算都可以看作是对底层性质之间某个逻辑符号的封装。

在本章最后一节 :numref:`第 %s 节 <powerset>` 中，我们把某个类型中的所有集合组成的集合族本身作为一种类型来研究。

.. include:: ch09_Sets/01_Sets.inc
.. include:: ch09_Sets/02_Set_Operations.inc
.. include:: ch09_Sets/03_Powerset.inc
""",
    "10_Relations.rst.txt": r"""
.. _relations:

关系
====

正如集合为一个类型中对象的性质提供了便利语言，*关系*也为一个类型中对象对的性质提供了便利语言。听起来这也许枯燥而抽象，但这样的性质在数学中无处不在：一个实数小于另一个实数；一个整数与另一个整数模 5 同余；一个集合是另一个集合的子集；一个函数是另一个函数的逆。

本章介绍关系本身可以具有的一些重要性质：关系可以是*自反*、*对称*、*反对称*或*传递*的，也可以具有这些性质的任意组合。

.. include:: ch10_Relations/01_Introduction.inc
.. include:: ch10_Relations/02_Equivalence_Relations.inc
""",
    "latexindex.rst.txt": r"""
测试用标题
==========

.. toctree::
   :maxdepth: 2

   00_Introduction
   01_Proofs_by_Calculation
   02_Proofs_with_Structure
   03_Parity_and_Divisibility
   04_Proofs_with_Structure_II
   05_Logic
   06_Induction
   07_Number_Theory
   08_Functions
   09_Sets
   10_Relations
   Index_of_Tactics
   Mainstream_Lean
""",
    "Index_of_Tactics.rst.txt": r"""
.. raw:: latex

    \appendix

.. _tactic_index:

Lean 策略索引
=============

标有 \* 的策略是本书专用的策略，因此你无法通过搜索引擎、网络论坛等渠道获得关于它们的帮助。请重读书中指出的相关部分，或询问你的教师。

.. rubric:: \* ``addarith``（首次使用：:numref:`第 %s 节 <shortcut>`）

试图通过把项从等式或不等式的一边移到另一边来证明该等式或不等式。

.. rubric:: ``apply``（首次使用：:numref:`第 %s 节 <lemmas>`；用于 :math:`\forall` 和 :math:`\to` 假设：:numref:`第 %s 节 <forall_implies>`）

调用指定的引理或假设来改变目标。

.. rubric:: ``by_cases``（首次使用：:numref:`第 %s 节 <lem>`）

按给定命题为真或为假进行分类讨论。

.. rubric:: \* ``cancel``（首次使用：:numref:`第 %s 节 <tactic_mode>`）

消去等式或不等式两边的公因子，消去两边共同出现的幂，等等。

.. rubric:: ``constructor``（首次使用：:numref:`第 %s 节 <and>`；用于 ``↔`` 目标：:numref:`第 %s 节 <iff>`）

把一个“且”目标（:math:`\land`）拆成分别对应左右两部分的子目标。

.. rubric:: ``contradiction``（首次使用：:numref:`第 %s 节 <contradiction_hyp>`）

若当前已有两个相互矛盾的假设，则结束证明。

.. rubric:: ``dsimp``（首次使用：:numref:`第 %s 节 <parity>`）

展开一个定义。它通常用于证明探索阶段，而不是用于最终版本；它有助于更仔细地查看目标或假设，但在多数情况下，删除一行 ``dsimp`` 后证明仍能成立。

.. rubric:: \* ``extra``（首次使用：:numref:`第 %s 节 <proving_inequalities>`；用于同余：:numref:`第 %s 节 <using_modular>`）

用于不等式或同余等其他关系的比较策略：它可以检查两边相差一个正量的不等式、两边相差 3 的倍数的模 3 同余，等等。

.. rubric:: ``interval_cases``（首次使用：:numref:`第 %s 节 <forall_implies>`）

给定一个自然数变量或整数变量 :math:`n`，并且已有关于 :math:`n` 的数值上下界时，对 :math:`n` 的每一种可能数值分别产生一个情形。

.. rubric:: ``intro``（首次使用：:numref:`第 %s 节 <forall_implies>`；用于 :math:`\lnot` 目标：:numref:`第 %s 节 <contradiction>`）

从目标中引入一个全称量化变量（:math:`\forall`）或一个蕴含（:math:`\to`）的前件；或者在证明否定（:math:`\lnot`）目标时，为了导出矛盾而假设其正向版本。

.. rubric:: ``left``（首次使用：:numref:`第 %s 节 <or>`）

选择“或”目标（:math:`\lor`）的左侧选项。

.. rubric:: ``have``（首次使用：:numref:`第 %s 节 <tactic_mode>`；配合引理使用：:numref:`第 %s 节 <or>`；引入新目标：:numref:`第 %s 节 <and>`）

记录一个事实（随后给出该事实的证明），然后这个事实会作为额外假设可供使用。

.. rubric:: ``mod_cases``（首次使用：:numref:`第 %s 节 <using_modular>`）

按照变量模指定数的余数来引入分类讨论。

.. rubric:: \* ``numbers``（首次使用：:numref:`第 %s 节 <proving_inequalities>`；配合 ``at`` 处理矛盾：:numref:`第 %s 节 <contradiction_hyp>`）

证明数值事实，例如 :math:`3\cdot 12 < 13 + 25` 或 :math:`3\cdot 5+1=4\cdot 4`。

.. rubric:: ``obtain``（首次用于 :math:`\lor`：:numref:`第 %s 节 <or>`；用于 :math:`\land`：:numref:`第 %s 节 <and>`；用于 :math:`\exists`：:numref:`第 %s 节 <exists>`）

拆解形如“或”（:math:`\lor`）、“且”（:math:`\land`）或“存在”（:math:`\exists`）的假设。

.. rubric:: ``push_neg``（首次使用：:numref:`第 %s 节 <negation_normalize>`）

把一个假设或目标转换为逻辑等价的形式，其中否定号被尽可能向内推进。

.. rubric:: ``rel``（首次使用：:numref:`第 %s 节 <proving_inequalities>`；用于同余：:numref:`第 %s 节 <using_modular>`；用于逻辑等价：:numref:`第 %s 节 <negation_normalize>`）

一个用于不等式或同余等其他关系的“类似代换”的策略：它会在目标中寻找某个指定不等式（或同余等）事实的左边，并在这种替换“显然”给出一个有效的不等式（或模算术等）推理时，把它替换为该事实的右边。可与 ``rw`` 比较。

.. rubric:: ``right``（首次使用：:numref:`第 %s 节 <or>`）

选择“或”目标（:math:`\lor`）的右侧选项。

.. rubric:: ``ring``（首次使用：:numref:`第 %s 节 <proving_equalities_in_lean>`）

解决代数等式目标，例如 :math:`(x + y) ^ 2 = x ^ 2 + 2xy + y ^ 2`，前提是证明实质上只是“展开两边并重新整理”。

.. rubric:: ``rw``（首次使用：:numref:`第 %s 节 <proving_equalities_in_lean>`；用于 ``↔`` 假设或引理：:numref:`第 %s 节 <iff>`）

代换：在目标中寻找某个指定等式事实的左边，并把它替换为该事实的右边。

对于 ``↔`` 假设或引理，把指定 ``↔`` 事实的左边替换为其右边。

.. rubric:: ``use``（首次使用：:numref:`第 %s 节 <exists>`）

为存在性目标（:math:`\exists`）提供一个见证。
""",
}


SOURCE_TEXTS.update({
    "00_Introduction.rst.txt": r"""
.. raw:: latex

    \frontmatter

.. _introduction:

前言
====

关于本书
--------

本书讨论如何书写细致而严谨的数学证明。本书配有以计算机形式化语言
`Lean <https://leanprover.github.io/about/>`__ 写成的代码。

本书关注的是证明技巧，而不是理论体系的建立：书中证明后还会在后文反复引用的定理并不多。
相反，本书的核心在于例题。正文中有两百多个带解答的问题作为例题，另有数百个无解答的问题留给读者练习。
每个问题和每个解答都同时以标准数学文字和 Lean 呈现（阅读本书时，应在计算机上打开相应的 Lean 代码文件）；
而对于刚接触证明的学生来说，这两种“语言”几乎同样陌生，因此大多数解答都附有非形式化的说明。


为什么使用 Lean？
----------------

几千年来，人们一直用文字表达数学论证。如今数学语言已经高度标准化，并形成了许多约定，
使数学家能够高效而无歧义地相互交流。本书的首要目标，是教你阅读和书写标准的数学文字。

称为 *交互式定理证明器* 的计算机系统（也称为 *证明助理*，或用于 *形式化* 的系统）
提供了表达数学论证的另一种方式。
`Lean <https://leanprover.github.io/>`_ 是其中一种系统；它是一个开源项目，
自 2013 年以来由 Microsoft Research 等机构开发。不过，这类系统早在
`计算机发展的早期 <https://en.wikipedia.org/wiki/Automath>`_ 就已经出现。

像 Lean 这样的交互式定理证明系统多年来已经变得越来越容易使用，但它们还远谈不上真正 *容易* 使用：
它们会像其他程序设计语言一样挑剔而严格。那么，为什么本书建议你在第一次接触证明时就使用这样的系统呢？

第一，如其名称所示，在交互式定理证明器中书写证明是交互式的。在证明的每个时刻，
你都可以看到 *证明状态* 的可视化表示：你已经知道什么（你的 *假设*），以及你当前要证明什么（你的 *目标*）。
如果你刚开始书写数学证明，可能会惊讶地发现，在纸上经历几步正向推理和反向推理的交替之后，
区分假设与目标并不容易；在分类讨论中，也很容易忘记某一个情形。Lean 实时更新的证明状态表示，
使你不必把这些信息全部放在工作记忆中。

第二，计算机形式化系统毕竟是严格而不宽容的程序设计语言；你一犯错，它们就会给出语法错误。
反馈是即时的，你可以不断迭代，直到得到可运行的内容。用 Lean 写出的解答保证是完全正确的：
不会在负号下错误地代换不等式，不会除以零，也不会在代数运算中漏掉项。这对于证明型数学尤其有用：
在微积分题中，若中途犯一个小错，后面的解答也许改动不大；但在证明中途犯一个小错，后面的论证可能就完全失效。

最后，你通过 *策略* 与 Lean 交互；每个策略执行某种推理方式中的一个步骤。
本教材教授的策略（其中一些是为本书专门编写的）各自构成本书心智世界中一个允许使用的推理“原子”。
这使得一件在纯文字教材中可能带有主观性的事情变得客观：什么算作一个细节完整的证明。
不仅如此，我提供给你的这些“原子”也被设计成会引导你采用某些数学论证结构风格 [#]_；
这些风格在标准数学文字中是惯常的，但学生往往需要较长时间才能自然采用。

本书是一部以 Lean 为工具的数学教材。它的设计目标是让 Lean 的学习曲线比数学本身更平缓 [#]_：
这部分依靠精心选择的练习，部分依靠使用我自己的一种 Lean“方言”，其中 Lean 词汇表 [#]_
受到限制，但又刚好足以满足本书的数学需要。（主要差异的摘要可见附录
:ref:`transitioning_to_regular_lean`。）我希望，在解题时，你的大部分智力努力都用于数学本身，
而不是用于 Lean 的实现细节或语法怪癖。

内容与预备知识
--------------

如果你（1）非常熟悉高中代数，并且（2）有学习执行复杂数学算法的经验，那么你已经准备好阅读本书了。
我心目中的典型读者，是刚学完 Calculus II 的大学一、二年级学生。但本书实际上不使用微积分。

本书最主要的新意是“双语”呈现：把文字数学与 Lean 代码并列。但这种呈现方式所要求的设计选择，
也在其他方面塑造了本书。

:numref:`第 %s 章 <proofs_by_calculation>` 对“计算式证明”作了格外细致的处理。
这样的证明之所以自然地成为本书起点，是因为它们很容易翻译成 Lean；但它们本身也值得重视，
因为这一层次的学生常常会在这类问题上遇到困难。 [#]_

:numref:`第 %s 章 <proofs_with_structure>` 和 :numref:`第 %s 章 <proofs_with_structure_ii>`
缓慢推进 `自然演绎 <https://en.wikipedia.org/wiki/Natural_deduction>`_ 规则，解决关于
:math:`\mathbb{N}`、:math:`\mathbb{Z}`、:math:`\mathbb{Q}` 和 :math:`\mathbb{R}` 的问题；
这些问题逐渐包含越来越多的逻辑联结词和量词。把一切都翻译成 Lean 的要求，
使本书在这些章节中保持严格诚实。典型的入门证明教材没有这道护栏，因此常会出现一些小的越界之处，
例如给出一个很好的分类证明例子，但其中暗中使用了尚未讲到的证明技巧，如为存在命题补上见证。

逻辑直到 :numref:`第 %s 章 <logic>` 才被明确讲授；到那时，读者已经熟悉各种逻辑联结词和量词，
也熟悉在文字与符号之间来回翻译数学陈述。因此，逻辑章可以相对简短，并把重点放在逻辑等价这一概念上
（主要用自然演绎来呈现，以便与 :numref:`第 %s 章 <proofs_with_structure>` 和
:numref:`第 %s 章 <proofs_with_structure_ii>` 衔接，而不是使用真值表）。 [#]_

本书其余章节更接近第一门证明课程通常会覆盖的内容。此时读者已经对 Lean 足够熟悉，
数学呈现也不再受到限制。

:numref:`第 %s 章 <parity_and_divisibility>` 讨论初等数论的基本概念。
该章只使用有限的推理工具，因此可以放在 :numref:`第 %s 章 <proofs_with_structure>` 和
:numref:`第 %s 章 <proofs_with_structure_ii>` 之间作为间歇。
后续章节中还会继续以数论定义和定理作为例子，而数论部分则在
:numref:`第 %s 章 <number_theory>` 以希腊数学的大结果作结：
素数有无穷多个、欧几里得引理以及二的平方根为无理数。

:numref:`第 %s 章 <induction>` 讨论归纳法。其处理相当全面，包括相对于
:math:`\mathbb{Z}`、:math:`\mathbb{N}\times \mathbb{N}` 和
:math:`\mathbb{Z}\times \mathbb{Z}` 上各种非平凡良基关系的归纳与递归。

最后，:numref:`第 %s 章 <functions>`、:numref:`第 %s 章 <sets>` 和
:numref:`第 %s 章 <relations>` 依次讨论函数、集合和关系。我们采取类型论观点：
函数是原始概念，而集合和关系则被定义为取值于
:math:`\left[\operatorname{true}/\operatorname{false}\right]` 的函数。

教师说明
--------

本书基于我在 2023 年春季于 Fordham University 教授的一门课程的讲义。
该课程有 20 名学生，主要是一、二年级学生，其中位背景是 Calculus II。
许多学生（但并非全部）也修过一门计算机编程入门课。

这门课每周两次，每次 75 分钟，共 13 周；在这段时间里覆盖了本书约 80% 的内容。
一次典型课堂结构可能如下：

* 25 分钟传统黑板讲授；
* 5 分钟屏幕共享讲授，在 Lean 中做同样的问题；
* 20 分钟学生两人一组在 Lean 中练习，教师巡视；
* 25 分钟传统黑板讲授，也许比前一段更偏理论。

这门课的作业可按需提供。作业相对较短（每周 5 到 7 题），但学生几乎必须同时以书面和 Lean 两种形式提交所有题目。
大多数学生需要在办公时间或通过电子邮件获得支持，才能完成这些作业。

课程还在第 5 周和第 10 周设置了口试。这些是一对一的 20 分钟面试，用来评估 Lean 熟练度：
学生现场解决此前未见过的 Lean 练习（每位学生的题目不同），并口头解释自己的推理。
课程成绩构成为：作业 25%，口试 20%，传统笔试 55%（一次期中和一次期末，二者完全不含 Lean）。

显然，课堂中教师巡视指导、办公时间和邮件中的作业支持、以及口试相结合，
意味着需要花相当多时间与单个学生（或小组学生）互动。学生与教师 20:1 的比例是可持续的。
我怀疑若要超过这一比例，就需要非常强的学生，或一位有经验且热情高涨的助教。

学生们在云端开发环境中运行 Lean，以免需要在自己的计算机上安装 Lean。
我使用的是 `Gitpod <https://www.gitpod.io/>`_（另一种选择是
`GitHub Codespaces <https://github.com/features/codespaces>`_）；如何开始使用 Gitpod，
可参见本书 `代码仓库 <https://github.com/hrmacbeth/math2001>`_ README 中的简短说明。
学生的 Lean 作业通过 `Gradescope <https://www.gradescope.com/>`_ 自动评分器自动评分
（另一种选择是 `GitHub Classroom <https://classroom.github.com/>`_）。
Lean 社区的 `教学建议网页 <https://leanprover-community.github.io/teaching/>`_
提供了搭建这类课程基础设施的说明和故障排查。

致谢
----

我由衷感谢

* Microsoft Research 提供了 `资助 <https://www.microsoft.com/en-us/research/academic-program/microsoft-research-lean-award-program/>`_，
  支持本书写作；
* Fordham 的本系允许我教授这门发展出本书的实验课程；
* 该课程 Math 2001 L01 Spring 2023 中勇敢尝试的学生们，感谢他们的热情与机智；
* Matthew Hertz 搭建了本书的 Sphinx 基础设施，并排版了最初几章；
* `mathlib 社区 <https://leanprover-community.github.io/>`_，特别是 Mario Carneiro、
  Gabriel Ebner、Scott Morrison、Thomas Murrills 和 David Renshaw，
  感谢他们在 2022 年秋至 2023 年冬进行 Lean 3 到 Lean 4 移植时，优先处理我课程所需的库内容；
* Mario Carneiro 还参与了多次长时间编程攻关，产出了本书中最有意思的一些定制策略；
* Jeremy Avigad、Rob Lewis 和 Patrick Massot 分享了 Lean 课程的技术基础设施，
  并与我多次讨论用 Lean 教授数学这一梦想。

.. rubric:: 脚注

.. [#] 例如，在大多数代数推理中使用计算块，以及偏好正向推理而不是反向推理。

.. [#] 如果你想要相反方向的教材，
  `Mathematics in Lean <https://leanprover-community.github.io/mathematics_in_lean/>`_
  是数学化 Lean 的标准入门书。但请注意，那本书预期读者有更多数学经验：
  即使只是证明初等命题，书写惯用的 Lean 代码也需要一定的数学成熟度。

.. [#] 用于代数推理的策略词汇包括 ``ring``、``rw``、
  ``numbers``（即 ``norm_num``）、``rel``（为本书定制编写，但现在已进入 mathlib 正式库）、
  ``extra``（定制编写）和 ``cancel``（定制编写）。它们足以处理整数上几乎所有代数推理，
  包括非线性不等式。本书在 :numref:`第 %s 节 <proving_equalities_in_lean>` 到
  :numref:`第 %s 节 <tactic_mode>` 中训练这种语汇，后来会带来回报：
  它避免了按名称调用无穷无尽的引理，例如 ``mul_le_mul_of_nonneg_left``、``pow_pos`` 或
  ``le_of_pow_le_pow``。其他定制自动化也会轻量地简化归纳原理、良基性证明、积类型和集合方面的工作。
  全书中按名称调用的引理总数不到五十个。

.. [#] 事实上，在许多入门证明课程中，即使没有真正掌握这种推理方式，
  也完全有可能应付大量以 *等式* 为主的推理；但若不掌握计算式证明，几乎不可能熟练处理 *不等式*。
  如果学生没有在入门证明课程中学会这一技巧，那么到实分析时，它会重新回来成为障碍。

.. [#] 有经验的读者也许会喜欢 :numref:`第 %s 节 <lem>` 中的问题；该节引入经典推理。
  这些问题（据我所知）是新的，而且比通常教材中的例子更初等。
""",
    "Mainstream_Lean.rst.txt": r"""
.. _transitioning_to_regular_lean:

过渡到主流 Lean
===============

如果你喜欢本书，也许会希望进一步使用 Lean，例如阅读
`Mathematics in Lean <https://leanprover-community.github.io/mathematics_in_lean/>`_，
或启动一个
`独立的形式化项目 <https://github.com/leanprover-community/mathlib4/wiki/Using-mathlib4-as-a-dependency>`_。

你会发现，本书使用的 Lean“方言”不同于 `mathlib <https://github.com/leanprover-community/mathlib4>`_
库及其相关文献（例如 *Mathematics in Lean*）中使用的主流数学 Lean。
为了帮助你适应，本附录概述主要差异。

本书中使用的一些策略，是 mathlib 中相应策略的有意弱化版本。我这样做，
是为了屏蔽 Lean 的某些能力，因为在本书层次的文字证明中，通常会把这些细节完整写出。
这些有意弱化的策略包括：

.. _tactic_comparison_table:

..  list-table::  本书策略及其 mathlib 原型
    :widths: 30 30 50
    :header-rows: 1

    * - mathlib 策略
      - 弱化的

        *证明的技艺*

        版本
      - 差异

    * - ``norm_num``
      - ``numbers``
      - ``norm_num`` 能完成本书要求读者手工完成的一些计算，

        包括模 :math:`n` 化简、

        处理逻辑，以及检查整除性和素性

    * - ``gcongr``
      - ``rel``
      - ``gcongr`` 不要求你说明正在代入哪些假设

    * - ``linarith``
      - ``addarith``
      - ``linarith`` 除了加减常数外，还可以取线性不等式的常数倍，

        可以组合许多线性不等式，且不要求你说明

        正在使用哪些假设

    * - ``duper``
      - ``exhaust``
      - ``duper`` 能处理包含量词的逻辑任务，而不只限于

        无量词的任务

本书中使用的一些策略在 mathlib 中没有直接对应物。它们通常是对一小组引理的封装；
在 mathlib 中，这些引理会按名称调用。

.. _tactic_lemma_wrapper_table:

..  list-table::  本书中没有 mathlib 对应物的策略
    :widths: 30 80
    :header-rows: 1

    * - *证明的技艺* 中的策略
      - 所封装的引理

    * - ``extra``
      - ``Int.modEq_fac_zero``、``le_add_of_nonneg_right``、

        ``lt_add_of_pos_right`` 等，以及策略

        ``positivity``

    * - ``cancel``
      - ``mul_left_cancel₀``、``lt_of_pow_lt_pow``、

        ``pos_of_mul_pos_left`` 等，以及策略

        ``positivity``

    * - ``simple_induction``

        ``induction_from_starting_point``

        ``two_step_induction``

        ``two_step_induction_from_starting_point``

      - ``Nat.le_induction``、``Nat.twoStepInduction`` 等，

        以及策略 ``induction`` 或 ``induction'``

本书中的许多问题若以 mathlib 风格的 Lean 来解，会高效得多，
因为某些步骤序列可以由超出本书数学范围的高级算法一步完成。应当了解的这类策略包括：

.. _decision_procedures:

..  list-table::  本书未使用的高级算法
    :widths: 30 30 50
    :header-rows: 1

    * - 算法
      - mathlib 策略
      - 该策略可以替代的步骤类型

    * - `Fourier-Motzkin 消元法 <https://en.wikipedia.org/wiki/Fourier%E2%80%93Motzkin_elimination>`_
      - ``linarith``
      - ``addarith``、``rel``、``ring``、``numbers``

    * - `Gröbner 基 <https://en.wikipedia.org/wiki/Gr%C3%B6bner_basis>`_
      - ``polyrith``
      - ``rw``、``ring``

    * - `叠加演算 <https://en.wikipedia.org/wiki/Superposition_calculus>`_
      - ``duper``
      - 证明或子证明末尾的逻辑策略

本书没有涉及的另一点，是如何与库交互。由于 mathlib 含有超过一百万行 Lean 代码，
要弄清库中是否已经有你想要的引理，并不总是容易的！在本书中，
我通过预先告诉你希望你使用的每个引理名称来避开这个问题。

与库交互时，需要了解以下几个基本点：

* `在线文档 <https://leanprover-community.github.io/mathlib4_docs/>`_ 通常比源代码更易读：
  它可搜索，并且含有内部超链接。
* 引理往往以极高的一般性陈述……:math:`(a - b) + c = a - (b - c)`
  `这个引理 <https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Basic.html#sub_sub>`_
  不是针对 :math:`\mathbb{R}` 陈述的，而是针对 ``SubtractionCommMonoid`` 陈述的。
  在修完抽象代数和点集拓扑的第一门课程之后，你可能会更容易与库交互。
* 如果你能猜出一个引理的精确陈述，策略 ``exact?`` 会在库中找到它。

以上只是触及皮毛：Lean 还有许多更多功能，可以帮助你进行数学探索。
*Mathematics in Lean*、`社区网站 <https://leanprover-community.github.io/>`_
和 `社区讨论区 <https://leanprover.zulipchat.com/>`_ 提供了进一步探索的指引。
祝你顺利探索！
""",
})


def main() -> None:
    for name, text in SOURCE_TEXTS.items():
        (SOURCES / name).write_text(text.strip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
