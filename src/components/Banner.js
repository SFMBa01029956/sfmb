import { useState, useEffect } from "react";
import { Container, Row, Col } from "react-bootstrap"
import { ArrowRightCircle } from "react-bootstrap-icons";
import headerImg from '../assets/img/header-img.svg';
import 'animate.css'
import TrackVisibility from 'react-on-screen';
import { isVisible } from "@testing-library/user-event/dist/utils";

export const Banner = () => {
  const [loopNum, setLoopNum] = useState(0);
  const [isDeleting, setIsDeleting] = useState(false);
  const toRotate = ["Software Developer", "Digital Artist", "Programmer", "Student"];
  const [text, setText] = useState('');
  const [delta, setDelta] = useState(300 - Math.random() * 100);
  const period = 2000;

  useEffect(() => {
    let ticker = setInterval(() => {
      tick();
    }, delta)

    return () => { clearInterval(ticker)};
  }, [text])

  const tick = () => {
    let i = loopNum % toRotate.length;
    let fullText = toRotate[i];
    let updatedText = isDeleting ? fullText.substring(0, text.length - 1) : fullText.substring(0, text.length + 1);

    setText(updatedText);

    if (isDeleting) {
      setDelta(prevDelta => prevDelta / 2);
    }

    if (!isDeleting && updatedText === fullText) {
      setIsDeleting(true);
      setDelta(period);
    } else if (isDeleting && updatedText === '') {
      setIsDeleting(false);
      setLoopNum(prevLoopNum => prevLoopNum + 1);
      setDelta(500);
    }
  }
  
  return (
    <section className="banner" id="home">
      <Container>
        <Row className="align-items-center">
          <Col xs={12} md={6} xl={7}>
            <TrackVisibility>
            {({ isVisible }) => 
              <div className={isVisible ? "animated__animated animate__fadeIn" : ""}>
                <span className="tagLine">Welcome to my Portfolio</span>
                <h1>{`Hi, I'm SFMB, `}<span className="wrap">{text}</span></h1>
                <p> Student at Tecnológico de Monterrey. I consider myself very curious. I like to push my creative skills by creating Pixel-art and music. Passionate about technological advancements, fine arts, and entertainment. I’m interested in AI, Full-stack Development, smart process solutions, game-dev, and optimization. </p>
                <button onClick={() => console.log('clicked')}>Let’s Connect<ArrowRightCircle size={25}/></button>
              </div>}
            </TrackVisibility>
          </Col>
          <Col xs={12} md={6} xl={5}>
            <img src={headerImg} alt="Header Img"/>
          </Col>
        </Row>
      </Container>
    </section>
  )
}