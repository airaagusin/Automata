# Finite Automata Diagrams

## 🟣 Moore Machine
The diagram below shows the **Moore Machine**, where the output depends only on the current state.

![Moore Machine Diagram](<img width="1277" height="1724" alt="deepseek_mermaid_20251105_a5d011" src="https://github.com/user-attachments/assets/19309852-710a-4608-ad7f-641c0df2f66f" />
)

**Explanation:**
    

    A [label="A"];
    B [label="B"];
    C [label="C"];
    D [label="D"];
    E [label="E"];

    // Transitions: input/output
    A -> A [label="0/A"];
    A -> B [label="1/B"];
    B -> C [label="0/A"];
    B -> D [label="1/B"];
    C -> D [label="0/C"];
    C -> B [label="1/B"];
    D -> B [label="0/B"];
    D -> C [label="1/C"];
    E -> D [label="0/C"];
    E -> E [label="1/C"];
}


---

## 🔵 Mealy Machine
The diagram below shows the **Mealy Machine**, where the output depends on both the state and the input.

![Mealy Machine Diagram](<img width="1563" height="1870" alt="deepseek_mermaid_20251105_6b2175" src="https://github.com/user-attachments/assets/6435bdd2-a2b8-4604-ba2d-0007d3fa25b4" />
)

**Explanation:**

    "Output A" [label="Output A"];
    "Output B" [label="Output B"];
    "Output C" [label="Output C"];

    // Transitions: input only (outputs belong to states)
    "Output A" -> "Output B" [label="1"];
    "Output A" -> "Output A" [label="0"];
    "Output B" -> "Output B" [label="0"];
    "Output B" -> "Output A" [label="1"];
    "Output B" -> "Output C" [label="0"];
    "Output C" -> "Output C" [label="1"];
    "Output C" -> "Output B" [label="0"];
}
