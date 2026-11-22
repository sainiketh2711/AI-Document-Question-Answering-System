# AI-Based Document Question Answering System

A Python-based document question-answering application that reads the University Library Guide, extracts structured information, and answers supported questions through rule-based retrieval and reasoning.

The system does not use a machine-learning or generative AI model. It uses regular expressions, a structured knowledge base, topic detection, and conditional calculations to produce answers.

## Features

- Loads the library guide from a text document
- Builds a structured knowledge base automatically
- Answers direct questions about:
  - Library opening and closing times
  - Weekday and weekend schedules
  - Student and faculty borrowing limits
  - Late fines
  - Membership and visitor privileges
  - Reference-book restrictions
  - Renewals and reservations
  - Library facilities
  - Computer-session limits
  - Public holidays
- Calculates fines from the number of books and overdue days
- Compares student and faculty borrowing rules
- Processes multiple questions in one input
- Handles unsupported questions with a clear response
- Includes automated unit tests

## Project Structure

```text
AI_Document_QA_Assignment/
|-- documents/
|   `-- library_guide.txt       # Source document
|-- screenshots/                # Application and test screenshots
|-- src/
|   |-- document_qa.py          # Application entry point
|   |-- knowledge_base.py       # Document parsing and extraction
|   |-- question_processor.py   # Question normalization and topic preparation
|   |-- reasoning_engine.py     # Answer generation and numerical reasoning
|   `-- reasoning_rules.py      # Topic keywords and question parsing rules
|-- tests/
|   `-- test_system.py          # Automated unit tests
`-- README.md
```

## Requirements

- Python 3.10 or later
- No third-party Python packages are required

## How to Run

From the project folder, run:

```powershell
python src/document_qa.py
```

The program displays the extracted knowledge base, then opens an interactive prompt:

```text
Enter your question: What are the library timings on weekends?
Enter your question: How much is the fine for 3 books overdue by 5 days?
Enter your question: exit
```

## Example Questions

```text
What are the weekday timings?
What are the library timings on Sundays?
How many books can students borrow?
What is the faculty borrowing limit?
Can visitors borrow books?
Can reference books be taken outside?
Can I renew a book if another member reserved it?
What is the fine for 3 books overdue by 5 days?
Compare student and faculty borrowing limits.
How long can I use a computer?
Is the library open on public holidays?
What facilities does the library provide?
```

Multiple questions can be entered together by separating them with punctuation or line breaks:

```text
What are the library timings? How many books can students borrow? What is the late fine?
```

## Running Tests

Run the automated test suite from the project root:

```powershell
python -m unittest tests/test_system.py -v
```

The tests cover:

- Document extraction
- Student and faculty borrowing rules
- Fine calculations
- Reference books and renewals
- Visitor membership
- Weekday and weekend timings
- Computer-session limits
- Public holidays
- Multiple questions
- Student/faculty comparison
- Unsupported questions

## How It Works

1. `document_qa.py` loads `documents/library_guide.txt`.
2. `knowledge_base.py` uses regular expressions to extract timings, limits, fines, facilities, and other values.
3. `reasoning_rules.py` normalizes questions and identifies relevant topics.
4. `reasoning_engine.py` retrieves the matching knowledge-base value, performs calculations when needed, and formats the answer.
5. The application continues accepting questions until the user enters `exit`.

## Limitations

- Extraction patterns are tailored to the wording and structure of the supplied library guide.
- The system supports the topics implemented in `reasoning_engine.py`.
- It does not perform semantic search or answer questions outside the knowledge base.
- Major changes to the source document may require updating extraction patterns.

## Sample Screenshots

Screenshots demonstrating the knowledge base, reasoning, unknown-question handling, and tests are stored in the [screenshots](screenshots/) directory.

## System Architecture
flowchart TD
    A[Input Document: Library Guide] --> B[Document Loading]
    B --> C[Information Extraction]
    C --> D[Knowledge Base Construction]

    E[User Question] --> F[Question Processing]
    F --> G[Topic Identification]
    G --> H[Information Retrieval]

    D --> H
    H --> I{Reasoning Required?}

    I -->|Yes| J[Rule-Based Reasoning]
    I -->|No| K[Direct Answer Generation]

    J --> L[Answer Generation]
    K --> L

    L --> M[Display Answer to User]

## Alogorithm
10. Algorithm

1. Start the system.
2. Locate the input document.
3. Check whether the document exists.
4. Read the document contents.
5. Convert the document text into a structured knowledge base.
6. Display the extracted knowledge base.
7. Accept a question from the user.
8. Check whether the user entered "exit".
9. If the user entered "exit", terminate the program.
10. Otherwise, process the question.
11. Identify the relevant topic using predefined keywords.
12. Retrieve the required information from the knowledge base.
13. Determine whether reasoning or calculation is required.
14. Perform the required reasoning.
15. Generate the answer.
16. Display the answer to the user.
17. Repeat steps 7–16 until the user exits.
18. Stop the system.

### Pseudocode
Pseudocode

BEGIN

    LOAD library guide document

    IF document does not exist
        DISPLAY error message
        STOP
    END IF

    READ document contents

    CREATE knowledge base from document

    IF knowledge base is empty
        DISPLAY error message
        STOP
    END IF

    DISPLAY knowledge base

    WHILE system is running

        INPUT user question

        IF question is "exit"
            STOP
        END IF

        IF question is empty
            DISPLAY input error
            CONTINUE
        END IF

        IDENTIFY question topics

        RETRIEVE relevant information

        IF reasoning is required
            PERFORM reasoning or calculation
        END IF

        GENERATE answer

        DISPLAY answer

    END WHILE

END

11. Testing and Evaluation

The system was evaluated using different test cases to verify document processing, knowledge base construction, question processing, information retrieval, reasoning, and answer generation.

Test Cases

Test Case| Input| Expected Result| Status
Document Loading| Run the main program| Document loads successfully| Pass
Knowledge Base Construction| Load the library guide| Relevant information is extracted and structured| Pass
Direct Question Answering| Ask about library timings| Correct library timings are retrieved| Pass
Numerical Reasoning| Calculate fine for overdue books| Correct fine is calculated| Pass
Student-Faculty Comparison| Compare borrowing limits| Correct limits and loan durations are provided| Pass
Multiple Questions| Enter multiple questions in one input| Answers are generated for the supported questions| Pass
Conditional Reasoning| Ask about book renewal restrictions| Answer considers reservation conditions| Pass
Unsupported Question| Ask about an unsupported facility| System handles unsupported information without fabricating an answer| Pass
Membership Information| Ask whether visitors can borrow books| Correct membership restriction is retrieved| Pass
Reference Book Restrictions| Ask whether reference books can be borrowed| Correct restriction is retrieved| Pass
Computer Usage| Ask about computer session duration| Correct duration and condition are retrieved| Pass
Automated Testing| Execute the test suite| Automated tests complete successfully| Pass

Evaluation

The system was evaluated based on the following criteria:

1. Document Processing: The system successfully loads the input document.
2. Information Extraction: Relevant information is extracted using regular expressions.
3. Knowledge Representation: Extracted information is stored in a structured knowledge base.
4. Question Processing: User questions are processed and relevant topics are identified.
5. Information Retrieval: Relevant information is retrieved from the knowledge base.
6. Reasoning: The system performs numerical calculations, comparisons, and conditional reasoning.
7. Answer Generation: Answers are generated based on the extracted information.
8. Error Handling: The system handles empty inputs, missing documents, and unsupported questions.

Result

The implemented system successfully demonstrates document-based question answering using information extraction, structured knowledge representation, rule-based retrieval, and reasoning. The tested functionalities produced the expected results for supported questions.

12. Limitations

1. Document Format: The current system primarily processes text documents and does not directly support complex formats such as scanned PDFs or images.

2. Pattern Dependency: Information extraction relies on predefined regular-expression patterns. Changes in document wording may affect extraction accuracy.

3. Domain Specificity: The question-answering system is designed around the information and topics available in the University Library Guide.

4. Limited Question Understanding: The system identifies question topics using predefined keywords rather than advanced natural language processing techniques.

5. Limited Knowledge Base: The system can only answer questions based on information extracted and represented in its knowledge base.

6. No Machine Learning Model: The system uses rule-based processing and reasoning instead of trained machine learning or large language models.

13. Future Enhancements

1. Multiple Document Formats: Support PDF, DOCX, and other document formats.

2. Advanced NLP: Integrate natural language processing techniques to improve question understanding.

3. Semantic Search: Implement semantic retrieval to identify relevant information even when the question wording differs from the document.

4. Machine Learning Integration: Incorporate machine learning or language models for more flexible answer generation.

5. Improved Knowledge Extraction: Develop more general extraction techniques that can work with different document structures and domains.

6. Graphical User Interface: Develop a user-friendly interface for uploading documents and interacting with the question-answering system.

7. Improved Evaluation: Use a larger dataset of questions and answers to evaluate accuracy, retrieval performance, and response quality.