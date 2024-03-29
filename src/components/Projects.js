import { Container, Row, Col, Nav, Tab } from "react-bootstrap";
import { ProjectCard } from "./ProjectCard";
import colorSharp2 from '../assets/img/color-sharp2.png';
import projImg1 from '../assets/img/project-img1.png';
import projImg2 from '../assets/img/project-img2.png';
import projImg3 from '../assets/img/project-img3.png';
import projImg4 from '../assets/img/project-img4.png';
import projImg5 from '../assets/img/project-img5.png';
import projImg6 from '../assets/img/project-img6.png';
import projImg7 from '../assets/img/project-img7.png';
import TrackVisibility from 'react-on-screen';

export const Projects = () => {

  const itesmProjects = [
    {
      title: "Ygneus - Serious Game",
      description: "Volcanic Projectile Motion Lab and Sim - 2020",
      imgUrl: projImg1,
    },
    {
      title: "Race Maker",
      description: "JACT 5TUDIO - Game for making racing tracks - 2021",
      imgUrl: projImg2,
    },
    {
      title: "Fiction Blog",
      description: "Creative Writing Blog - 2021",
      imgUrl: projImg6,
      href: "https://a01029956.blogspot.com/",
    }
  ]
  const gameJamProjects = [
    {
      title: "Anemic Panic",
      description: '"Everything is Backwards" Submission for the Coding Blocks Game Jam 2023',
      imgUrl: projImg3,
      href: "https://munij.itch.io/anemic-panic",
    },
    {
      title: "Catamari Catastrophe",
      description: '"You\'ve got to be kitten me!" Submission for the Jame Gam 26 Game Jam 2023',
      imgUrl: projImg7,
      href: "https://munij.itch.io/catamari",
    },
    {
      title: "Kaiju Clash",
      description: '"You are the Monster" Submission for the Mini Jam 127 Game Jam 2023',
      imgUrl: projImg5,
      href: "https://luisjakg.itch.io/kaiju-clash",
    }
  ]
  const personalProjects = [
    {
      title: "Art Instagram Account",
      description: "Ongoing collection of digital and plastic arts",
      imgUrl: projImg4,
      href: "https://www.instagram.com/thefirefrog88/",
    }
  ]

  return (
    <section className="project" id="projects">
      <Container>
        <Row>
          <Col size={12}>
            <TrackVisibility>
              {({ isVisible }) => 
              <div className={isVisible ? "animate__animated animate__fadeIn" : ""}>
                <h2>Projects</h2>
                <p> Some of the work i'm most proud of. Many projects were developed along with my peers at ITESM, others with my friends in Game Jams, and some others by myself as a complement to my professional profile.</p> 
                <Tab.Container id="projects-tabs" defaultActiveKey="first">
                  <Nav variant="pills" className="nav-pills mb-5 justify-content-center align-items-center" id="pills-tab">
                    <Nav.Item>
                      <Nav.Link eventKey="first">ITESM</Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                      <Nav.Link eventKey="second">Game Jams</Nav.Link>
                    </Nav.Item>
                    <Nav.Item>
                      <Nav.Link eventKey="third">Personal</Nav.Link>
                    </Nav.Item>
                  </Nav>
                  <Tab.Content id="slideInUp" className={isVisible ? "animate__animated animate__slideInUp" : ""}>
                    <Tab.Pane eventKey="first">
                      <Row>
                        {
                          itesmProjects.map((project, index) => {
                            return (
                              <ProjectCard
                                key={index}
                                {...project}
                              />
                            )
                          })
                        }
                      </Row>
                    </Tab.Pane>
                    <Tab.Pane eventKey="second">
                      <Row>
                        {
                          gameJamProjects.map((project, index) => {
                            return (
                              <ProjectCard
                                key={index}
                                {...project}
                              />
                            )
                          })
                        }
                      </Row>
                    </Tab.Pane>
                    <Tab.Pane eventKey="third">
                      <Row>
                        {
                          personalProjects.map((project, index) => {
                            return (
                              <ProjectCard
                                key={index}
                                {...project}
                              />
                            )
                          })
                        }
                      </Row>
                    </Tab.Pane>
                  </Tab.Content>
                </Tab.Container>
              </div>}
            </TrackVisibility>
          </Col>
        </Row>
      </Container>
      <img className="background-image-right" src={colorSharp2} alt=""/>
    </section>
  )
}