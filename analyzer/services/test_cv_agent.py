from analyzer.services.cv_agent import CVAnalyzerAgent

PDF_PATH = "media/cvs/test_cv.pdf"
TARGET_POSITION = "Backend Developer"


def run_test():
    agent = CVAnalyzerAgent()
    result = agent.analyze(PDF_PATH, TARGET_POSITION)
    print(result)
